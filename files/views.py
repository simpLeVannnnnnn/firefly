from django.shortcuts import render
from files.models import File
from django.http import StreamingHttpResponse

def big_file_download(request):
    
    id = request.POST
    file = File.objects.get(id=id)

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
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)

    return response
