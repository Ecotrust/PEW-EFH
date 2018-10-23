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
        ('close', 'close'),
        ('reopen', 'Reopen'),
        ('reopen', 'reopen'),
        ('reopen', 'open'),
        ('reopen', 'Open'),
        ('other', 'Other'),
        ('other', 'other'),
        ('none', 'None'),
        ('none', 'none')
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

        def m2_to_mi2(area_m2):
            return format_precision(float(area_m2) / 2590000.0, 0)

        def get_total_area(geoqs):
            area_m2 = 0
            for result in geoqs:
                area_m2 += result.geometry.transform(2163, clone=True).area
            return m2_to_mi2(area_m2)

        def within_max_percent(val1, val2):
            ratio = float(val1)/float(val2)
            if ratio > (1-settings.MAX_DETAIL_REPORT_AREA_VARIANCE) and ratio < (1 + settings.MAX_DETAIL_REPORT_AREA_VARIANCE):
                return True
            else:
                return False

        # Call get_summary_reports with intersecting Grid Cells
        attributes['all'] = []
        total_area_sq_mi = m2_to_mi2(self.true_area_m2)
        attributes['all'].append({'title': 'Total Area', 'data': '%s sq mi' % total_area_sq_mi})
        if total_area_sq_mi < settings.MAX_DETAIL_REPORT_AREA_SQMI:
            aggregate_attributes = {}
            grid_cells = intersecting_cells(self.geometry_orig)
            drawing_grid_cells = intersecting_drawing_cells(self.geometry_orig)
            if drawing_grid_cells.count() > 0 and drawing_grid_cells.count() < settings.MAX_INTERSECTING_CELLS:
                if within_max_percent(get_total_area(drawing_grid_cells), total_area_sq_mi):
                    get_summary_reports(grid_cells, attributes['all'])
                    get_drawing_summary_reports(drawing_grid_cells, attributes['all'])
                    for (idx, strata) in enumerate(settings.REPORT_STRATA):
                        if strata in settings.STRATA_MAP.keys():
                            attributes[strata] = {}
                            for key in settings.STRATA_MAP[strata].keys():
                                stratum = settings.STRATA_MAP[strata][key]
                                attributes[strata][stratum] = []
                                stratum_cells = drawing_grid_cells.filter(**{strata: key})
                                get_drawing_summary_reports(stratum_cells, attributes[strata][stratum], True)

    @property
    def serialize_attributes(self):
        attributes = []
        if self.reg_action and not self.reg_action == 'none':
            attributes.append({'title': 'Regulatory Action', 'data': self.reg_action})
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        try:
            attributes += simplejson.loads(self.summary)['all']
            return { 'event': 'click', 'attributes': attributes }
        except simplejson.JSONDecodeError as e:
            print(str(e))
            self.save()
            return self.serialize_attributes

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

        attributes = {}
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
        num_val = re.findall(r"[-+]?\d*\.\d+|\d+",field['data'])
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
            val = sum(val_list)
            if unit_type == int and type(val) == float:
                val = int(round(val))
            return {
                'label': "%s%s" % (str(val), text),
                'values': [val],
                'text': [text]
            }
        if method == 'min':
            val = min(val_list)
            if unit_type == int and type(val) == float:
                val = int(round(val))
            return {
                'label': "%s%s" % (str(val), text),
                'values': [val],
                'text': [text]
            }
        if method == 'max':
            val = max(val_list)
            if unit_type == int and type(val) == float:
                val = int(round(val))
            return {
                'label': "%s%s" % (str(val), text),
                'values': [val],
                'text': [text]
            }
        if method == 'minmax':
            if len(val_list) > 0:
                min_list = [float(x) for (x,y) in val_list]
                max_list = [float(y) for (x,y) in val_list]
                min_val = unit_type(round(min(min_list)))
                max_val = unit_type(round(max(max_list)))
                if len(min_list) > 0 and len(max_list) > 0:
                    return {
                        'label': "%s%s%s%s" % (str(min_val), text[0], str(max_val), text[1]),
                        'values': [min_val, max_val],
                        'text': text
                    }
                else:
                    return False
            else:
                return False
        if method == 'mean':
            total_area = sum([area for (value, area) in val_list])
            numerator_list = [value*area for (value, area) in val_list]
            if len(numerator_list) > 0:
                val = str(unit_type(sum(numerator_list)/total_area))
                return {
                    'label': "%s%s" % (val, text),
                    'values': [val],
                    'text': [text]
                }
            else:
                return False
        return False

    def generate_summary_value(self, attributes, name, field):
        data = self.aggregate_values(field['values'], field['aggregate'], field['unit'], field['type'])
        if data:
            attributes.append({'title': name,'data': data})

    def summary_reports(self, attributes, strata='all', stratum={'all':'all'}):
        stratum_key = stratum.keys()[0]
        stratum_name = stratum[stratum_key]
        if not self.is_loading:
            from datetime import datetime
            feature_set = list(enumerate(self.feature_set(), start=1))
            count = len(feature_set)
            val_collector = {}
            for field in settings.COMPARISON_FIELD_LOOKUP:
                val_collector[field['name']] = field
                val_collector[field['name']]['values'] = []
            stratum_fields = {}
            for field in settings.STRATUM_COMPARISON_FIELD_LOOKUP:
                stratum_fields[field['name']] = field
            for (index, feature) in feature_set:
                if strata == 'all':
                    feature_summary = eval(feature.summary)[strata]
                else:
                    if not strata in eval(feature.summary).keys():
                        feature.save()
                    feature_summary = eval(feature.summary)[strata][stratum_name]
                feature_area = feature.true_area_m2
                for field in feature_summary:
                    if strata == 'all':
                        clean_val = self.clean_summary_value(field, val_collector[field['title']], feature_area)
                    else:
                        clean_val = self.clean_summary_value(field, stratum_fields[field['title']], feature_area)
                    if field['title'] == 'Total Area':
                        if feature.reg_action == 'close':
                            val_collector['Total Area Closed']['values'].append(clean_val)
                        elif feature.reg_action == 'reopen':
                            val_collector['Total Area Reopened']['values'].append(clean_val)
                    val_collector[field['title']]['values'].append(clean_val)
            for key in [x['name'] for x in settings.COMPARISON_FIELD_LOOKUP]:
                self.generate_summary_value(attributes,key,val_collector[key])
        else:
            attributes.append(eval(settings.SUMMARY_DEFAULT))

    @property
    def serialize_attributes(self):
        return self.serialize_strata_attributes('all')

    def serialize_strata_attributes(self, strata='all', stratum={'all':'all'}):
        attributes = []
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        self.summary_reports(attributes, strata, stratum)
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
    strata_3x3 = models.IntegerField(null=True, blank=True)
    strata_5x5 = models.IntegerField(null=True, blank=True)
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
