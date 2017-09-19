from django.shortcuts import render


def search(request, search_key):

    render(request, 'search.html', locals())