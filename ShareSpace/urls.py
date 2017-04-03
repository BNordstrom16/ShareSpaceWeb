from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^current_storages$', views.current_storages, name='current_storages'),
    url(r'^create/', login_required(views.create_storage), name='create_storage')

]

