from django import forms
from files.models import File


class FlieForm(forms.Form):

    title = forms.CharField(required=True)
    FileField = forms.FileField()

