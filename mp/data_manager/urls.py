from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    (r'^layer/([A-Za-z0-9_-]+)$', update_layer),
    (r'^layer', create_layer),
    (r'^wa_config', load_config),
    (r'^get_json/([\w-]*)', get_json),
    (r'^import_layer/?$', import_layer),
    (r'import_layer/(?P<uid>[\w_]+)/json/$', get_import_layer_json),
    (r'import_layer/(?P<layer_id>[\w_]+)/delete/$', delete_import_layer),
    (r'import_layer/share_import_layer/$', share_import_layer),
)
