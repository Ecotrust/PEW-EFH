from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    (r'^send', send_feedback),
    # (r'^bookmark', send_bookmark),
)
