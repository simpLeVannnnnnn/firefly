from django.shortcuts import render
from django.conf.urls import patterns, url
from upload import views


urlpatterns = patterns('',
    url(r'^$', views.upload, name='upload'),
)
