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

        #TODO: Remove this - we want to see orig, but here for drawing PUG testing
        # self.geometry_final = self.clip_to_grid(True)
        super(AOI, self).save(*args, **kwargs) # Call the "real" save() method

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

    def summary_reports(self, attributes):
        from datetime import datetime
        from ofr_manipulators import intersecting_drawing_cells
        grid_cells = False
        drawing_grid_cells = False
        total_area= 0
        # print("=======================")
        # print("Beginning looping though features")
        feature_set = list(enumerate(self.feature_set(), start=1))
        count = len(feature_set)
        for (index, feature) in feature_set:
            # index = fset[0]
            # feature = fset[1]

            # print("FEATURE %d of %d: ----------------------------------" % (index, count))
            total_area += feature.true_area_m2
            # TODO: can we tune this by just calling each feature's `summary_reports` method?
            # now = datetime.now()
            # print("     getting cells................ %s:%s:%s" % (now.hour, now.minute, now.second))
            if grid_cells:
                grid_cells = grid_cells | intersecting_cells(feature.geometry_orig)
            else:
                grid_cells = intersecting_cells(feature.geometry_orig)
            # now = datetime.now()
            # print("     aggregating cells............ %s:%s:%s" % (now.hour, now.minute, now.second))
            if drawing_grid_cells:
                drawing_grid_cells = drawing_grid_cells | intersecting_drawing_cells(feature.geometry_orig)
            else:
                drawing_grid_cells = intersecting_drawing_cells(feature.geometry_orig)
            # print("     done......................... %s:%s:%s" % (now.hour, now.minute, now.second))
        attributes.append({'title': 'Total Area', 'data': str(format_precision(float(total_area) / 2590000.0, 0)) + ' sq mi'})
        # now = datetime.now()
        # print("Cell count: %s ...........%s:%s:%s" % (str(len(grid_cells)),now.hour, now.minute, now.second))
        # print("Generating Summary report..... %s:%s:%s" % (now.hour, now.minute, now.second))
        if grid_cells:
            get_summary_reports(grid_cells, attributes)
        if drawing_grid_cells:
            get_drawing_summary_reports(drawing_grid_cells, attributes)

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
