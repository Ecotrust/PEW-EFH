from django.db import models
from utils import get_domain
from django.template.defaultfilters import slugify
#from sorl.thumbnail import ImageField
from madrona.features.models import FeatureCollection, SpatialFeature, Feature
from madrona.features import register
from django.contrib.gis.db.models import GeometryField
from django.conf import settings

class TOCThemeOrder(models.Model):
    theme = models.ForeignKey("TOCTheme")
    order = models.IntegerField(default=0)
    toc = models.ForeignKey('TOC', blank=True, null=True)

class TOC(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode('%s' % (self.name))

class TOCTheme(models.Model):
    display_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100, help_text="This field should be a 'slugified' version of Display Name (must start with a letter and should only contain letters (a-z or A-Z), digits (0-9), hyphens(-), and underscores(_))")
    description = models.TextField(blank=True, null=True)
    layers = models.ManyToManyField("Layer", blank=True, null=True)
    # order = models.IntegerField(default=0)

    def TOC(self):
        # import pdb
        # pdb.set_trace()
        #return self.toc_set.all()[0]
        return "\n".join([toc_theme_order.toc.name for toc_theme_order in self.tocthemeorder_set.all()])

    def __unicode__(self):
        return unicode('%s' % (self.name))

    @property
    def toDict(self):
        layers = [layer.id for layer in self.layers.filter(is_sublayer=False).exclude(layer_type='placeholder')]
        themes_dict = {
            'id': self.id,
            'display_name': self.display_name,
            'layers': layers,
            'description': self.description,
            'is_toc_theme': True
        }
        return themes_dict


class Theme(models.Model):
    display_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    header_image = models.CharField(max_length=255, blank=True, null=True)
    header_attrib = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(max_length=255, blank=True, null=True)

    factsheet_thumb = models.CharField(max_length=255, blank=True, null=True)
    factsheet_link = models.CharField(max_length=255, blank=True, null=True)

    # not really using these atm
    feature_image = models.CharField(max_length=255, blank=True, null=True)
    feature_excerpt = models.TextField(blank=True, null=True)
    feature_link = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode('%s' % (self.name))

    @property
    def learn_link(self):
        domain = get_domain(8000)
        return '%s/learn/%s' %(domain, self.name)

    @property
    def toDict(self):
        layers = [layer.id for layer in self.layer_set.filter(is_sublayer=False).exclude(layer_type='placeholder')]
        themes_dict = {
            'id': self.id,
            'display_name': self.display_name,
            'learn_link': self.learn_link,
            'layers': layers,
            'description': self.description
        }
        return themes_dict

class Layer(models.Model):
    TYPE_CHOICES = (
        ('XYZ', 'XYZ'),
        ('WMS', 'WMS'),
        ('ArcRest', 'ArcRest'),
        ('MapBox', 'MapBox'),
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
        ('Vector', 'Vector'),
        ('placeholder', 'placeholder'),
    )
    name = models.CharField(max_length=244)
    slug_name = models.CharField(max_length=244, blank=True, null=True)
    layer_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    url = models.TextField(blank=True, null=True, default=None)
    shareable_url = models.BooleanField(default=True, help_text="Shareable (non-vector) layers will offer a Tiles link")
    proxy_url = models.BooleanField(default=False, help_text="proxy layer url through marine planner")
    arcgis_layers = models.CharField(max_length=255, blank=True, null=True, help_text="IDs separated by commas (no spaces)")
    wms_slug = models.CharField(max_length=255, blank=True, null=True)
    sublayers = models.ManyToManyField('self', blank=True, null=True)
    themes = models.ManyToManyField("Theme", blank=True, null=True)
    is_sublayer = models.BooleanField(default=False)
    legend = models.CharField(max_length=255, blank=True, null=True, help_text="Path to Legend Image file (http://somewhere.com/legend.png)")
    legend_title = models.CharField(max_length=255, blank=True, null=True, help_text="If no value is entered, the layer name will be used as the Legend Title")
    legend_subtitle = models.CharField(max_length=255, blank=True, null=True)
    utfurl = models.CharField(max_length=255, blank=True, null=True, help_text="For XYZ MBTiles this should be the same URL as entered above, but ending with .grid.json rather than .png")
    utfjsonp = models.BooleanField(default=False, help_text="For MBTiles, check this box")
    summarize_to_grid = models.BooleanField(default=False)
    filterable = models.BooleanField(default=False)
    proj = models.CharField(max_length=255, blank=True, null=True, help_text="will be EPSG:3857, if unspecified")
    #tooltip
    description = models.TextField(blank=True, null=True)

    #data description (updated fact sheet) (now the Learn pages)
    data_overview = models.TextField(blank=True, null=True)
    data_source = models.CharField(max_length=255, blank=True, null=True)
    data_notes = models.TextField(blank=True, null=True)

    #data catalog links
    bookmark = models.CharField(max_length=755, blank=True, null=True)
    map_tiles = models.CharField(max_length=255, blank=True, null=True)
    kml = models.CharField(max_length=255, blank=True, null=True)
    data_download = models.CharField(max_length=255, blank=True, null=True, help_text="Link to download the data")
    metadata = models.CharField(max_length=255, blank=True, null=True, help_text="Link to the metadata")
    source = models.CharField(max_length=255, blank=True, null=True, help_text="Link to the data providers")

    #geojson javascript attribution
    EVENT_CHOICES = (
        ('click', 'click'),
        ('mouseover', 'mouseover')
    )
    attribute_title = models.CharField(max_length=255, blank=True, null=True, help_text="If no value is entered, the layer name will be used as the header for the Attribute list (triggered on click events)")
    attribute_fields = models.ManyToManyField('AttributeInfo', blank=True, null=True)
    compress_display = models.BooleanField(default=False)
    attribute_event = models.CharField(max_length=35, choices=EVENT_CHOICES, default='click', help_text="Only 'click' is available at this time")
    lookup_field = models.CharField(max_length=255, blank=True, null=True)
    lookup_table = models.ManyToManyField('LookupInfo', blank=True, null=True)
    vector_color = models.CharField(max_length=7, blank=True, null=True, help_text="Outline color represented in a hex format (e.g. #00ff00)")
    vector_fill = models.FloatField(blank=True, null=True, help_text="Fill opacity represented by a floating point value (e.g. '.8')")
    vector_graphic = models.CharField(max_length=255, blank=True, null=True)
    opacity = models.FloatField(default=.5, blank=True, null=True)

    #mapbox fields
    enable_mapbox_id = models.BooleanField(default=False, help_text="Enable click identification on MapBox layer")
    mapbox_tileset_id = models.CharField(max_length=255, null=True, blank=True, default=None)
    mapbox_access_token = models.CharField(max_length=255, null=True, blank=True, default=settings.MAPBOX_ACCESS_TOKEN, help_text="Put your id here if your URL doesn't have 'access_token=' in it")

    def __unicode__(self):
        return unicode('%s' % (self.name))

    @property
    def is_parent(self):
        return self.sublayers.all().count() > 0 and not self.is_sublayer

    @property
    def parent(self):
        if self.is_sublayer:
            return self.sublayers.all()[0]
        return self

    @property
    def sublayer_list(self):
        if self.is_parent:
            return self.sublayers.all().order_by('name')
        else:
            return None

    @property
    def slug(self):
        return slugify(self.name)

    @property
    def data_overview_text(self):
        if not self.data_overview and self.is_sublayer:
            return self.parent.data_overview
        else:
            return self.data_overview

    @property
    def data_source_text(self):
        if not self.data_source and self.is_sublayer:
            return self.parent.data_source
        else:
            return self.data_source

    @property
    def data_notes_text(self):
        if not self.data_notes and self.is_sublayer:
            return self.parent.data_notes
        else:
            return self.data_notes

    @property
    def bookmark_link(self):
        if not self.bookmark and self.is_sublayer and self.parent.bookmark:
            return self.parent.bookmark.replace('<layer_id>', str(self.id))
        if not self.bookmark:
            domain = get_domain(8000)
            return '%s/planner/#%s' %(domain, self.slug)
        return self.bookmark

    @property
    def data_download_link(self):
        if self.data_download and self.data_download.lower() == 'none':
            return None
        if not self.data_download and self.is_sublayer:
            return self.parent.data_download
        else:
            return self.data_download

    # Originally the structure of this method was similar to others (e.g. data_download_link and source_link)
    # but those aren't making sense to me right now so I'm changing the structure of this one
    # Eventually this method should change back to reflect the others, or the others should be changed to reflect this method
    @property
    def metadata_link(self):
        if self.metadata:
            return self.metadata
        if self.is_sublayer:
            return self.parent.metadata_link
        if self.layer_type == 'ArcRest':
            try:
                return self.url.replace('/export', '/info/metadata')
            except AttributeError as e:
                pass
        return None

    @property
    def source_link(self):
        if self.source and self.source.lower() == 'none':
            return None
        if not self.source and self.is_sublayer:
            return self.parent.source
        else:
            return self.source

    @property
    def description_link(self):
        theme_name = self.themes.all()[0].name
        domain = get_domain(8000)
        return '%s/learn/%s#%s' %(domain, theme_name, self.slug)

    @property
    def tiles_link(self):
        if self.is_shareable and self.layer_type in ['XYZ', 'ArcRest', 'WMS']:
            domain = get_domain(8000)
            return '%s/explore/%s' %(domain, self.slug)
        return None

    @property
    def tooltip(self):
        if self.description and self.description.strip() != '':
            return self.description
        elif self.parent.description and self.parent.description.strip() != '':
            return self.parent.description
        else:
            return None

    @property
    def is_shareable(self):
        if self.shareable_url == False:
            return False
        if self.parent and self.parent.shareable_url == False:
            return False
        return True

    @property
    def serialize_attributes(self):
        return {'title': self.attribute_title,
                'compress_attributes': self.compress_display,
                'event': self.attribute_event,
                'attributes': [{'display': attr.display_name, 'field': attr.field_name, 'precision': attr.precision} for attr in self.attribute_fields.all().order_by('order')]}

    @property
    def serialize_lookups(self):
        return {'field': self.lookup_field,
                'details': [{'value': lookup.value, 'color': lookup.color, 'dashstyle': lookup.dashstyle, 'fill': lookup.fill, 'graphic': lookup.graphic} for lookup in self.lookup_table.all()]}

    @property
    def toDict(self):
        sublayers = [
            {
                'id': layer.id,
                'name': layer.name,
                'type': layer.layer_type,
                'url': layer.url,
                'arcgis_layers': layer.arcgis_layers,
                'wms_slug': layer.wms_slug,
                'utfurl': layer.utfurl,
                'utfjsonp': layer.utfjsonp,
                'proxy_url': layer.proxy_url,
                'proj': layer.proj,
                'summarize_to_grid': layer.summarize_to_grid,
                'parent': self.id,
                'legend': layer.legend,
                'legend_title': layer.legend_title,
                'legend_subtitle': layer.legend_subtitle,
                'description': layer.tooltip,
                'overview': layer.data_overview_text,
                'data_source': layer.data_source,
                'data_notes': layer.data_notes,
                'kml': layer.kml,
                'data_download': layer.data_download_link,
                'metadata': layer.metadata_link,
                'source': layer.source_link,
                'tiles': layer.tiles_link,
                'attributes': layer.serialize_attributes,
                'lookups': layer.serialize_lookups,
                'color': layer.vector_color,
                'fill_opacity': layer.vector_fill,
                'graphic': layer.vector_graphic,
                'opacity': layer.opacity,
                'enable_mapbox_id': layer.enable_mapbox_id,
                'mapbox_tileset_id': layer.mapbox_tileset_id,
                'mapbox_access_token': layer.mapbox_access_token
            }
            for layer in self.sublayers.all()
        ]
        layers_dict = {
            'id': self.id,
            'name': self.name,
            'type': self.layer_type,
            'url': self.url,
            'arcgis_layers': self.arcgis_layers,
            'wms_slug': self.wms_slug,
            'utfurl': self.utfurl,
            'utfjsonp': self.utfjsonp,
            'proxy_url': self.proxy_url,
            'proj': self.proj,
            'subLayers': sublayers,
            'legend': self.legend,
            'legend_title': self.legend_title,
            'legend_subtitle': self.legend_subtitle,
            'description': self.description,
            'overview': self.data_overview,
            'data_source': self.data_source,
            'data_notes': self.data_notes,
            'summarize_to_grid': self.summarize_to_grid,
            'kml': self.kml,
            'data_download': self.data_download_link,
            'metadata': self.metadata_link,
            'source': self.source_link,
            'tiles': self.tiles_link,
            'attributes': self.serialize_attributes,
            'lookups': self.serialize_lookups,
            'color': self.vector_color,
            'fill_opacity': self.vector_fill,
            'graphic': self.vector_graphic,
            'opacity': self.opacity,
            'enable_mapbox_id': self.enable_mapbox_id,
            'mapbox_tileset_id': self.mapbox_tileset_id,
            'mapbox_access_token': self.mapbox_access_token
        }
        return layers_dict

    def save(self, *args, **kwargs):
        self.slug_name = self.slug
        super(Layer, self).save(*args, **kwargs)

@register
class ImportLayer(FeatureCollection):
    # name = models.CharField(max_length=244)
    # legend = models.CharField(max_length=255, blank=True, null=True, default=None, help_text="Path to Legend Image file (http://somewhere.com/legend.png)")
    # legend_title = models.CharField(max_length=255, blank=True, null=True, default=None, help_text="If no value is entered, the layer name will be used as the Legend Title")
    description = models.TextField(blank=True, null=True, default=None)

    def __unicode__(self):
        return unicode(self.name)

    def toDict(self):
        url = '/data_manager/import_layer/%s/json/' % self.uid
        groups = [x.name for x in self.sharing_groups.all()]
        if len(groups) > 0:
            shared = True
            sharedByName = self.user.get_full_name()
            sharedByUsername = self.user.username
        else:
            shared = False
            sharedByName = None
            sharedByUsername = None
        layer_dict = {
            'name': self.name,
            'type': 'Vector',
            'url': url,
            'proj': 'EPSG:3857',
            'sublayers': [],
            'description': self.description,
            'color': settings.DEFAULT_UPLOAD_LAYER_COLOR_HEX,
            'fill_opacity': 1,
            'opacity': 0.6,
            'id': 'il%s' % self.id,
            'selected_groups': groups,
            'shared': shared,
            'sharedByName': sharedByName,
            'sharedByUsername': sharedByUsername,
            'uid': self.uid,
        }
        return layer_dict

    def geojson(self):
        import json as simplejson
        geojson_dict = {
            'name': self.name,
            'type': "FeatureCollection",
            'crs': {
                'type': "name",
                'properties': {
                    "name": "EPSG:3857"
                }
            },
            'features': []
        }
        for feat in self.feature_set():
            try:
                geom = simplejson.loads(feat.geometry_final.geojson)
            except Exception as e:
                print("======== %s ========" % str(e))
                geom = simplejson.loads(feat.geometry_orig.geojson)
                pass
            try:
                properties = simplejson.loads(feat.summary)
            except Exception as e:
                print("======== %s ========" % str(e))
                properties = {}
                pass
            feature_dict = {
                "type": "Feature",
                'geometry': geom,
                'properties': properties
            }
            geojson_dict['features'].append(feature_dict)
        return simplejson.dumps(geojson_dict)

    class Options:
        verbose_name = 'Imported Layer'
        # icon_url = 'img/aoi.png'
        export_png = False
        manipulators = []
        # manipulators = ['drawing.manipulators.ClipToPlanningGrid']
        # optional_manipulators = ['clipping.manipulators.ClipToShoreManipulator']
        form = 'data_manager.forms.ImportLayerForm'
        # form_template = 'aoi/form.html'
        # show_template = 'aoi/show.html'
        valid_children = (
            'data_manager.models.ImportFeature',
            # 'scenarios.models.Scenario'
        )

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
class ImportFeature(GeometryFeature):
    summary = models.TextField(blank=True, null=True, default=settings.SUMMARY_DEFAULT)

    class Options:
        verbose_name = 'Imported Feature'
        # icon_url = 'img/aoi.png'
        export_png = False
        manipulators = []
        # manipulators = ['drawing.manipulators.ClipToPlanningGrid']
        # optional_manipulators = ['clipping.manipulators.ClipToShoreManipulator']
        form = 'data_manager.forms.ImportFeatureForm'
        # form_template = 'aoi/form.html'
        # show_template = 'aoi/show.html'


class AttributeInfo(models.Model):
    display_name = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    precision = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return unicode('%s' % (self.field_name))

class LookupInfo(models.Model):
    DASH_CHOICES = (
        ('dot', 'dot'),
        ('dash', 'dash'),
        ('dashdot', 'dashdot'),
        ('longdash', 'longdash'),
        ('longdashdot', 'longdashdot'),
        ('solid', 'solid')
    )
    value = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    dashstyle = models.CharField(max_length=11, choices=DASH_CHOICES, default='solid')
    fill = models.BooleanField(default=False)
    graphic = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode('%s' % (self.value))


class DataNeed(models.Model):
    name = models.CharField(max_length=100)
    archived = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    expected_date = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    themes = models.ManyToManyField("Theme", blank=True, null=True)

    @property
    def html_name(self):
        return self.name.lower().replace(' ', '-')

    def __unicode__(self):
        return unicode('%s' % (self.name))
