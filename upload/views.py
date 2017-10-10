#coding=UTF-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from files.forms import FlieForm
from files.models import File
from upload.service import handle_uploaded_file, handle_uploaded_file_cover
import os


def upload_file(request):
    if request.method == 'POST':
        form = FlieForm(request.POST, request.FILES)
        if form.is_valid():
            obj = File()
            
            f = request.FILES['FileField']
            cover = request.FILES['cover']
            handle_uploaded_file(f)
            handle_uploaded_file_cover(cover)
            
            obj.title = form.cleaned_data['title']
            obj.introduction = form.cleaned_data['introduction']
            obj.FileField = f
            obj.cover = cover
            obj.size = f.size
            obj.unique_name = f.name
            obj.save()

            return HttpResponseRedirect('/upload/success/')
        
    else:
        form = FlieForm()
        return render(request, 'upload.html', locals())

def upload_success(request):
    return render(request, 'success.html')
