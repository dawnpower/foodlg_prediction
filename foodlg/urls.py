from django.conf.urls import include, url
from django.conf import settings

from django.views.static import serve
from django.contrib import admin

urlpatterns = [
    url(r'^'+settings.SITE_PREFIX+r'api/', include('foodlg.api.urls',namespace="api")),
    url(r'^'+settings.SITE_PREFIX, include('foodlg.core.urls',namespace="core")),
    url(r'^'+settings.SITE_PREFIX+r'admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns +=[  
        url(r'^'+settings.SITE_PREFIX+r'(?P<path>favicon\..*)$',serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^'+settings.SITE_PREFIX+r'media/(?P<path>.*)$' , serve, {'document_root': settings.MEDIA_ROOT}),
    ] 