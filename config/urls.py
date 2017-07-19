from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'users.views.index'),
    url(r'^home/', 'users.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('upload.urls')),
    url(r'^login/$', 'users.views.login'),
    url(r'^regist/$', 'users.views.regist'),
    url(r'^index/$', 'users.views.index'),
    url(r'^logout/$', 'users.views.logout'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
