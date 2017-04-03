from django.shortcuts import render
from .models import Storage
from django_tables2 import RequestConfig
from .tables import StorageTable


def index(request):
    current_user = request.user.username
    return render(request, '../templates/index.html', {'name': current_user})


def about(request):
    return render(request, '../templates/about.html', {})


def current_storages(request):
    table = StorageTable(Storage.objects.all())
    RequestConfig(request).configure(table)
    return render(request, '../templates/current_storages.html', {'table': table})


def create_storage(request):
    return render(request, '../templates/create_storage.html', {})






