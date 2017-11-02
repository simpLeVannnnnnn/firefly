from django.conf.urls import patterns, url
from haystack.views import SearchView
from search.views import MySeachView

urlpatterns = [
    url(r'^$', MySeachView(), name='haystack_search'),
]