from django.contrib import admin
from files.models import File,Category,Tag
class YourAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updata_time',)
admin.site.register([File, Category, Tag])