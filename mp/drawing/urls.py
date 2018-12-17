from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    #drawings
    url(r'get_drawings$', get_drawings),
    url(r'delete_design/(?P<uid>[\w_]+)/$', delete_drawing), #user deletes drawing (or cancels empty geometry result)
    url(r'get_attributes/(?P<uid>[\w_]+)/$', get_attributes), #get attributes for a given scenario
    url(r'get_geometry_orig/(?P<uid>[\w_]+)/$', get_geometry_orig), #get geometry_orig wkt
    url(r'clip_to_grid$', get_clipped_shape),
    url(r'copy_collection/(?P<uid>[\w_]+)/$', copy_collection),

    url(r'get_collections$', get_collections),
    url(r'get_collection_attributes/(?P<uid>[\w_]+)/$', get_collection_attributes),
    url(r'delete_collection/(?P<uid>[\w_]+)/$', delete_collection),

    #feature reports
    # url(r'wind_report/(\d+)', wind_analysis, name='wind_analysis'), #user requested wind energy site analysis
    url(r'aoi_report/(\d+)', aoi_analysis, name='aoi_analysis'), #user requested area of interest analysis

)
