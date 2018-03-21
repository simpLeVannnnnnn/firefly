#coding=UTF-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from files.forms import FlieForm
from files.models import File
from upload.service import handle_uploaded_file, handle_uploaded_file_cover, data_processing
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
            obj.category = form.cleaned_data['category']
            obj.introduction = form.cleaned_data['introduction']
            obj.developer = form.cleaned_data['developer']
            obj.tag = form.cleaned_data['tag']
            obj.support_system = form.cleaned_data['support_system']
            obj.language = form.cleaned_data['language']
            obj.version = form.cleaned_data['version']  
            obj.author = request.user.username
            obj.FileField = f
            obj.cover = cover
            obj.size = f.size/(1024**2)
            obj.unique_name = f.name
            obj.save()
            predata = list(File.objects.all())
            data_processing(predata, obj)
            return HttpResponseRedirect('/upload/success/')
        else:
            form = FlieForm()
            return render_to_response('upload.html',RequestContext(request,{'errors': u'请正确填写', 'form':form}))
        
    else:
        form = FlieForm()
        return render(request, 'upload.html', locals())

def upload_success(request):
    return render(request, 'success.html')
