from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from files.models import File, Tag, Category


def home(request):
    files = File.objects.all()
    tags = Tag.objects.all()

    high_score_files = File.objects.order_by('-score', 'title')

    paginator1 = Paginator(high_score_files, 9)
    high_score_files = paginator1.page(1)

    paginator2 = Paginator(files, 9)
    files = paginator2.page(1)

    return render(request, 'first_load_home.html', locals())

def about(request):
    return render(request, 'about.html')

def high_score(request):
    return render(request, 'high_score.html')

def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    category = tag.category
    files = File.objects.filter(tag=tag, category=category)
    tags = Tag.objects.filter(category=category)

    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        files = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        files = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())

def index(request):
    files = File.objects.all()
    tags = Tag.objects.all()

    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return render(request, 'index.html', locals())
    

def picture(request):
    category = get_object_or_404(Category, unique_name='picture')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)

    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return render(request, 'index.html', locals())

def info(request):
    category = get_object_or_404(Category, unique_name='info')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)
    
    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())

def application(request):
    category = get_object_or_404(Category, unique_name='application')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)

    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())

def document(request):
    category = get_object_or_404(Category, unique_name='document')
    files = File.objects.filter(category=category)
    tags = Tag.objects.filter(category=category)

    paginator = Paginator(files, 12)
    page = request.GET.get('page')
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())
