from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^current_storages$', views.current_storages, name='current_storages'),
    url(r'^create/', views.create_storage, name='create_storage'),

]

