#coding=UTF-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from files.forms import FlieForm
from files.models import File
import os


def upload(request):
    if request.method == "POST":
        obj = FlieForm(request.POST,request.FILES)
        if obj.is_valid():
            
            FileField = request.FILES.get('FileField', None)
            f = open(os.path.join(".\\library",FileField.name),'wb+')    
            for chunk in FileField.chunks():      
                f.write(chunk)  
            f.close()

            url = "/library/%s" % FileField.name

            return render_to_response('file_list.html',{'url':url})
    else:
        obj = FlieForm()
    return render_to_response('upload.html',{'obj':obj})
