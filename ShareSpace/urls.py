from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^current_storages.html$', views.current_storages, name='current_storages')
]