from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    (r'^get_legend_json/(?P<url>)$', getLegendJSON),
    url(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
)
