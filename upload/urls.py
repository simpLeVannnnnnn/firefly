from django.shortcuts import render
from django.conf.urls import patterns, url
from upload import views


urlpatterns = patterns('',
    url(r'^$', views.upload_file, name='upload'),
    url(r'^success/$', views.upload_success, name='success'),
)
