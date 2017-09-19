from django.shortcuts import render, get_object_or_404
from files.models import File, Tag, Category

def home(request):
    files = File.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', locals())

def about(request):
    return render(request, 'about.html')

def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    category = tag.category
    files = File.objects.filter(tag=tag, category=category)
    tags = Tag.objects.filter(category=category)
    return render(request, 'index.html', locals())

def index(request):
    files = File.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', locals())

def picture(request):
    category = get_object_or_404(Category, unique_name='picture')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)
    return render(request, 'index.html', locals())

def info(request):
    category = get_object_or_404(Category, unique_name='info')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)
    return render(request, 'index.html', locals())

def application(request):
    category = get_object_or_404(Category, unique_name='application')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)
    return render(request, 'index.html', locals())

def document(request):
    category = get_object_or_404(Category, unique_name='document')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)
    return render(request, 'index.html', locals())
