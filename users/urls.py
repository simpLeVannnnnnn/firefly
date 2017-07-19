from django.shortcuts import render
from django.conf.urls import patterns, url
from users import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
)