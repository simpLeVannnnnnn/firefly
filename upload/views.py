from django.shortcuts import render
from files.models import File
# Create your views here.

class FlieForm(forms.Form):
    title = forms.CharField()
    url = forms.FileField()

def upload(request):
    if request.method == "POST":
        uf = FlieForm(request.POST,request.FILES)
        if uf.is_valid():
            title = uf.cleaned_data['title']
            url = uf.cleaned_data['url']
            new_file.title = title
            new_file.url = url
            new_file.save()
            return HttpResponse('upload ok!')
    else:
        uf = FlieForm()
    return render_to_response('upload.html',{'uf':uf})