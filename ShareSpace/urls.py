from django.conf.urls import url
from . import views
from .models import Storage


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^current_storages', views.current_storages, name='current_storages'),
    url(r'^create/', views.create_storage, name='create_storage'),
    url(r'^storage/(?P<storage_id>\d+)/', views.storage, name='storage'),
    url(r'^image/(?P<storage_id>\d+)/', views.show_image, name='show_image')

]

