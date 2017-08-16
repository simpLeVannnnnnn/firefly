from django.shortcuts import render
from django.conf.urls import patterns, url
from files import views


urlpatterns = patterns('',
    url(r'^(?P<file_id>\d+)', views.detail),
    url(r'^download/(?P<file_id>\d+)',views.file_download)
)