from django.conf.urls import patterns, url
from haystack.views import SearchView

urlpatterns = [
    url(r'^$', SearchView(), name='haystack_search'),
]