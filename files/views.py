#coding:utf-8

from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseRedirect
from files.models import File, Tag
from django.http import StreamingHttpResponse, HttpResponse
import os

def big_file_download(request, file_id):
    
    file = get_object_or_404(File,pk=file_id)

    file_name = file.unique_name

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(file_name))
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response

def file_download2(request, file_id):
    
        file = get_object_or_404(File,pk=file_id)
        file.amount_of_downloads += 1
        file.save()
        response = HttpResponse(file, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment;filename=%s' % os.path.split('/library/library/files/' + file.unique_name)[-1]
        return response

def file_download(request, file_id):

    file = get_object_or_404(File,pk=file_id)
    file.amount_of_downloads += 1
    file.save()
    return HttpResponseRedirect('/library/library/files/%s' % file.unique_name)

def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    return render(request, 'file_detail2.html', locals())

def file_delete(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file.delete()
    return render(request, 'success.html', locals())




