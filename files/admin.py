from django.contrib import admin
from files.models import File,Category,Tag

admin.site.register([File, Category, Tag])