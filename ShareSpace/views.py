from django.shortcuts import render
from .models import Storage

def index(request):
    return render(request, '../templates/index.html', {})

def about(request):
    return render(request, '../templates/about.html', {})

def current_storages(request):
    storage = Storage.objects.order_by('area_code')
    return render(request, '../templates/current_storages.html', {'Storage': storage})
