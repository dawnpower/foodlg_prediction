from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^demo$', views.demo,name='demo'),
    url(r'^example$', views.example,name='example'),
]
