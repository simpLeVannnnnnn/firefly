from django.shortcuts import render
from django.conf.urls import patterns, url
from users import views


urlpatterns = patterns('',
    url(r'^upload', views.upload, name='upload'),
)