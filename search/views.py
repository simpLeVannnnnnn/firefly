# encoding: utf-8
from django.shortcuts import render
from haystack.views import SearchView  
from files.models import *


def search(request, search_key):

    render(request, 'search.html', locals())


class MySeachView(SearchView):  
    def extra_context(self):       #重载extra_context来添加额外的context内容  
        context = super(MySeachView,self).extra_context()  
        side_list = File.objects.order_by('title')[:8]  
        context['side_list'] = side_list  
        return context 