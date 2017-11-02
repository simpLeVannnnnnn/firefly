# encoding: utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from users.forms import UserForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from files.models import File, Tag


def regist(request):

    if request.method=='POST':
        registerForm = RegisterForm(request.POST)
        username=request.POST.get('username','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        email=request.POST.get('email','')
        

        filterResult=User.objects.filter(username=username)
        if len(filterResult)>0:
            registerForm=RegisterForm()
            return render_to_response("regist.html",RequestContext(request,{'errors': u"用户已注册"}))
        user=User()
        user.username=username
        user.set_password(password1)
        user.email=email
        user.save()

        newUser=authenticate(username=username,password=password1)
        if newUser is not None:
            login(request, newUser)
            files = File.objects.all()
            tags = Tag.objects.all()
            return render_to_response('first_load_home.html',RequestContext(request), locals())

    return render_to_response('regist.html',RequestContext(request))

def login_view(request):

    if request.method=='POST':
        username=request.POST.get('username',)
        password=request.POST.get('password',)
        user = authenticate(username=username, password=password)
        if user is None:
            return render_to_response('login.html',RequestContext(request,{'errors': u'您的密码有误，请重新输入'}))
        if user.is_active:
            login(request, user)
            files = File.objects.all()
            tags = Tag.objects.all()
            return render(request, 'first_load_home.html', locals())
            # return render_to_response('home.html',RequestContext(request,{'username':username, 'file':files}))
        else:
            return render_to_response('login.html',RequestContext(request,{'errors': u'用户被冻结'}))
    else:
        uf = UserForm()
    return render_to_response('login.html',RequestContext(request,{'uf':uf}))


def logout_view(request):
    logout(request)
    files = File.objects.all()
    tags = Tag.objects.all()
    return render(request, 'first_load_home.html', locals())

