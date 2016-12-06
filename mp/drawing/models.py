from django.db import models
from django.utils.html import escape
from madrona.features import register
from madrona.features.models import PolygonFeature, FeatureCollection, MultiPolygonFeature, SpatialFeature, Feature
from madrona.common.utils import LargestPolyFromMulti, clean_geometry
from general.utils import sq_meters_to_sq_miles, format_precision
from ofr_manipulators import clip_to_grid, intersecting_cells
from reports import get_summary_reports, get_drawing_summary_reports
import settings
from django.contrib.gis.db.models import GeometryField, PointField, MultiPolygonField, GeoManager
import simplejson

class GeometryFeature(SpatialFeature):
    geometry_orig = GeometryField(srid=settings.GEOMETRY_DB_SRID,
            null=True, blank=True, verbose_name="Original Polygon Geometry")
    geometry_final = GeometryField(srid=settings.GEOMETRY_DB_SRID,
            null=True, blank=True, verbose_name="Final Polygon Geometry")

    @property
    def centroid_kml(self):
        """
        KML geometry representation of the centroid of the polygon
        """
        geom = self.geometry_final.point_on_surface.transform(settings.GEOMETRY_CLIENT_SRID, clone=True)
        return geom.kml


    class Meta(Feature.Meta):
        abstract = True

@register
class AOI(GeometryFeature):
    import settings
    ACTION_CHOICES = (
        ('close', 'Close'),
        ('reopen', 'Reopen'),
        ('other', 'Other'),
        ('none', 'None')
    )
    description = models.TextField(null=True,blank=True)
    reg_action = models.CharField(max_length=30, blank=True, null=True, choices=ACTION_CHOICES, default='none')
    summary = models.TextField(blank=True, null=True, default=settings.SUMMARY_DEFAULT)

    @property
    def is_loading(self):
        if self.summary == settings.SUMMARY_DEFAULT:
            return True
        return False

    @property
    def true_area_m2(self):
        return self.geometry_orig.transform(2163, clone=True).area

    @property
    def true_area_final_m2(self):
        return self.geometry_final.transform(2163, clone=True).area

    @property
    def formatted_area(self):
        return int((self.area_in_sq_miles * 10) +.5) / 10.

    @property
    def area_in_sq_miles(self):
        return sq_meters_to_sq_miles(self.true_area_final_m2)

    def summary_reports(self, attributes):
        from ofr_manipulators import intersecting_drawing_cells
        # Call get_summary_reports with intersecting Grid Cells
        attributes.append({'title': 'Total Area', 'data': str(format_precision(float(self.true_area_m2) / 2590000.0, 0)) + ' sq mi'})
        grid_cells = intersecting_cells(self.geometry_orig)
        get_summary_reports(grid_cells, attributes)
        drawing_grid_cells = intersecting_drawing_cells(self.geometry_orig)
        get_drawing_summary_reports(drawing_grid_cells, attributes)

    @property
    def serialize_attributes(self):
        attributes = []
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        attributes += simplejson.loads(self.summary)
        return { 'event': 'click', 'attributes': attributes }

    @classmethod
    def fill_color(self):
        return '776BAEFD'

    @classmethod
    def outline_color(self):
        return '776BAEFD'

    def clip_to_grid(self, drawing=False):
        geom = self.geometry_orig
        clipped_shape = clip_to_grid(geom, drawing)
        if clipped_shape:
            return LargestPolyFromMulti(clipped_shape)
        else:
            return clipped_shape

    def save(self, *args, **kwargs):
        # TODO Toggle clipping drawings to grid in settings
        # self.geometry_final = self.clip_to_grid()

        self.geometry_final = self.geometry_orig
        if self.geometry_final:
            self.geometry_final = clean_geometry(self.geometry_final)

        if not self.id:  #first save - if part of a large import, now is not a good time to calculate the summary
            super(AOI, self).save(*args, **kwargs) # Call the "real" save() method
        else:
            attributes = []
            self.summary_reports(attributes)
            self.summary = simplejson.dumps(attributes)
            super(AOI, self).save(*args, **kwargs) # Call the "real" save() method


    class Options:
        verbose_name = 'Area of Interest'
        icon_url = 'img/aoi.png'
        export_png = False
        manipulators = []
        # manipulators = ['drawing.manipulators.ClipToPlanningGrid']
        # optional_manipulators = ['clipping.manipulators.ClipToShoreManipulator']
        form = 'drawing.forms.AOIForm'
        form_template = 'aoi/form.html'
        show_template = 'aoi/show.html'


@register
class Collection(FeatureCollection):
    description = models.TextField(null=True,blank=True)

    class Options:
        verbose_name = 'Collection of Proposed Scenarios'
        form = 'drawing.forms.CollectionForm'
        form_template = 'collection/form.html'
        show_template = 'collection/show.html'
        valid_children = (
            'drawing.models.AOI',
            'scenarios.models.Scenario'
        )

    @property
    def is_loading(self):
        ret_val = False
        for feature in self.feature_set():
            if feature.is_loading:
                feature.save()
                ret_val = True
        return False

    def clean_summary_value(self, field, field_map, weight=1):
        import re
        method = field_map['aggregate']
        ret_type = field_map['type']
        num_val = re.findall(r'\d+',field['data'])
        if method in ['sum', 'min', 'max']:
            return ret_type(num_val[0])
        elif method in ['mean', 'minmax']:
            if method == 'mean':
                return (ret_type(num_val[0]), weight)
            if method == 'minmax':
                return (ret_type(num_val[0]),ret_type(num_val[1]))
        else:
            return (ret_type(num_val),False)

    def aggregate_values(self, val_list, method, text, unit_type):
        if method == 'sum':
            return "%s%s" % (str(sum(val_list)), text)
        if method == 'min':
            return "%s%s" % (str(min(val_list)), text)
        if method == 'max':
            return "%s%s" % (str(max(val_list)), text)
        if method == 'minmax':
            min_list = [x for (x,y) in val_list]
            max_list = [y for (x,y) in val_list]
            if len(min_list) > 0 and len(max_list) > 0:
                return "%s%s%s%s" % (str(min(min_list)), text[0], str(max(max_list)), text[1])
            else:
                return False
        if method == 'mean':
            total_area = sum([area for (value, area) in val_list])
            numerator_list = [value*area for (value, area) in val_list]
            if len(numerator_list) > 0:
                return "%s%s" % (str(unit_type(sum(numerator_list)/total_area)), text)
            else:
                return False

    def generate_summary_value(self, attributes, name, field):
        data = self.aggregate_values(field['values'], field['aggregate'], field['unit'], field['type'])
        if data:
            attributes.append({'title': name,'data': data})

    def summary_reports(self, attributes):
        if not self.is_loading:
            from datetime import datetime
            feature_set = list(enumerate(self.feature_set(), start=1))
            count = len(feature_set)
            summary_dict = {
                'name': self.name,
                'description': self.description
            }
            val_collector = {}
            for field in settings.COMPARISON_FIELD_LOOKUP:
                val_collector[field['name']] = field
                val_collector[field['name']]['values'] = []
            for (index, feature) in feature_set:
                feature_summary = eval(feature.summary)
                feature_area = feature.true_area_m2
                for field in feature_summary:
                    clean_val = self.clean_summary_value(field, val_collector[field['title']], feature_area)
                    val_collector[field['title']]['values'].append(clean_val)
            for key in [x['name'] for x in settings.COMPARISON_FIELD_LOOKUP]:
                self.generate_summary_value(attributes,key,val_collector[key])
        else:
            attributes.append(eval(settings.SUMMARY_DEFAULT))

    @property
    def serialize_attributes(self):
        attributes = []
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        self.summary_reports(attributes)
        return { 'event': 'click', 'attributes': attributes }

    def feature_set(self, recurse=False, feature_classes=None):
        return super(Collection, self).feature_set(recurse, feature_classes)

    def save(self, rerun=True, *args, **kwargs):
        # Foothold to manage save logic outside of Madrona - may not be necessary with overriding the form post url/view
        super(Collection, self).save(*args, **kwargs) # Call the "real" save() method

class GridCell(models.Model):

    gridcode = models.IntegerField(null=True, blank=True)
    sq_mi = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    # Substrate unit: sq miles
    hrd_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    mix_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    sft_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    rck_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    # Technically this is the depth of the centroid of the unit, but small enough to treat planning units as discrete
    depth = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    # PHS unit: sq miles
    hsall1_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall2_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall3_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall4_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr1_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr2_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr3_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    unique_id = models.IntegerField(null=True, blank=True)

    centroid = PointField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True,
        blank=True
    )

    geometry = MultiPolygonField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True, blank=True,
        verbose_name="Grid Cell Geometry"
    )
    objects = GeoManager()
