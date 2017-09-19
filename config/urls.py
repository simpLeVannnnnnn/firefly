from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'page.views.home'),
    url(r'^home/', 'page.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('upload.urls')),
    url(r'^login/$', 'users.views.login_view'),
    url(r'^regist/$', 'users.views.regist'),
    url(r'^index/$', 'page.views.index'),
    url(r'^about/$', 'page.views.about'),
    url(r'^picture/$', 'page.views.picture'),
    url(r'^info/$', 'page.views.info'),
    url(r'^application/$', 'page.views.application'),
    url(r'^document/$', 'page.views.document'),
    url(r'^logout/$', 'users.views.logout_view'),
    url(r'^files/',include('files.urls')),
    url(r'^tag/',include('page.urls')),
    url(r'^search/',include('haystack.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
