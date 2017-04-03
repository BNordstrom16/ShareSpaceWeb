from django.shortcuts import render
from .models import Storage
from django_tables2 import RequestConfig
from .tables import StorageTable
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, '../templates/index.html', {})


def about(request):
    return render(request, '../templates/about.html', {})


def current_storages(request):
    table = StorageTable(Storage.objects.all())
    RequestConfig(request).configure(table)
    return render(request, '../templates/current_storages.html', {'table': table})


@login_required(login_url='/accounts/login')
def create_storage(request):
    return render(request, '../templates/create_storage.html', {})







