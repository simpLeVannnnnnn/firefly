from django.conf.urls import patterns, url
from page import views


urlpatterns = patterns('',
    url(r'^(?P<tag_id>\d+)', views.tag),

)