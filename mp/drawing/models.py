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
    description = models.TextField(null=True,blank=True)

    @property
    def formatted_area(self):
        return int((self.area_in_sq_miles * 10) +.5) / 10.

    @property
    def area_in_sq_miles(self):
        return sq_meters_to_sq_miles(self.geometry_final.area)

    def summary_reports(self, attributes):
        from ofr_manipulators import intersecting_drawing_cells
        # Call get_summary_reports with intersecting Grid Cells
        attributes.append({'title': 'Total Area (Drawn)', 'data': str(format_precision(float(self.geometry_orig.area) / 2590000.0, 0)) + ' sq mi'})
        grid_cells = intersecting_cells(self.geometry_orig)
        get_summary_reports(grid_cells, attributes)
        drawing_grid_cells = intersecting_drawing_cells(self.geometry_orig)
        get_drawing_summary_reports(drawing_grid_cells, attributes)

    @property
    def serialize_attributes(self):
        attributes = []
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        # attributes.append({'title': 'Area', 'data': '%s sq miles' %format_precision(self.area_in_sq_miles, 2)})
        self.summary_reports(attributes)
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
        from itertools import chain
        grid_cells = False
        for feature in self.feature_set():
            if grid_cells:
                grid_cells = grid_cells | intersecting_cells(feature.geometry_orig)
            else:
                grid_cells = intersecting_cells(feature.geometry_orig)
        if grid_cells:
            get_summary_reports(grid_cells, attributes)

    @property
    def serialize_attributes(self):
        attributes = []
        if self.description:
            attributes.append({'title': 'Description', 'data': self.description})
        # attributes.append({'title': 'Area', 'data': '%s sq miles' %format_precision(self.area_in_sq_miles, 2)})
        self.summary_reports(attributes)
        return { 'event': 'click', 'attributes': attributes }

    def feature_set(self, recurse=False, feature_classes=None):
        return super(Collection, self).feature_set(recurse, feature_classes)

    def save(self, rerun=True, *args, **kwargs):
        # Foothold to manage save logic outside of Madrona - may not be necessary with overriding the form post url/view
        super(Collection, self).save(*args, **kwargs) # Call the "real" save() method

class GridCell(models.Model):

    gridcode = models.IntegerField(null=True, blank=True)
    #TODO: Of what?
    count = models.IntegerField(null=True, blank=True)
    sq_mi = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    #TODO: What unit?
    hrd_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    mix_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    sft_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    rck_sub_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    #TODO: mean, min, or max? Unit?
    depth = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    #TODO: Unit?
    hsall1_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall2_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall3_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hsall4_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr1_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr2_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    hssclr3_m2 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    #TODO: What is this?
    flag1 = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    shape_length = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
    #TODO: Unit?
    shape_area = models.DecimalField(null=True, blank=True, decimal_places=11, max_digits=16)
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
