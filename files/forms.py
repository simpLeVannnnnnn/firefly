from django import forms
from files.models import File,Category


class FlieForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('title', 'FileField', 'category', 'cover', 'version', 'bit', 'developer', 'support_system', 'language')


