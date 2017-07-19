from django import forms
from users.models import User

class UserForm(forms.Form): 
    username = forms.CharField()
    password = forms.CharField()
