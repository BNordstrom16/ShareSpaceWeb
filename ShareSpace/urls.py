from django.conf.urls import url
from . import views
from .views import EditStorage, DeleteStorage


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^current_storages', views.current_storages, name='current_storages'),
    url(r'^create/', views.create_storage, name='create_storage'),
    url(r'^image/(?P<storage_id>\d+)/', views.show_image, name='show_image'),
    url(r'^storage/(?P<storage_id>\d+)/', views.storage, name='storage'),
    url(r'^storage/edit/(?P<pk>[0-9]+)/', EditStorage.as_view(), name='storage_edit'),
    url(r'^storage/delete/(?P<pk>[0-9]+)/', DeleteStorage.as_view(), name='storage_delete')

]

