# -*-coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form): 
    username = forms.CharField(label=u"用户名", error_messages={'required': '请输入用户名'})
    password1 = forms.CharField(label=u"请输入密码", error_messages={'required': '请确认密码'})
    password2 = forms.CharField(label=u"请再次输入密码", error_messages={'required': '请确认密码'})
    email = forms.CharField(label=u"邮箱", error_messages={'required': '请输入邮箱'})


class UserForm(forms.Form): 
    username = forms.CharField(label=u"用户名", error_messages={'required': '请输入用户名'})
    password = forms.CharField(label=u"请输入密码", error_messages={'required': '请输入密码'})
