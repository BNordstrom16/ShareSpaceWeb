from django.shortcuts import render, redirect
from .models import Storage
from django_tables2 import RequestConfig
from .tables import StorageTable
from django.contrib.auth.decorators import login_required
from .forms import StorageForm


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
    if request.method == "POST":
        form = StorageForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.user_id = request.user
            model_instance.save()
            return redirect('/current_storages')
    else:
        form = StorageForm()

    return render(request, '../templates/create_storage.html', {'form': form})


def storage(request, storage_id):
    storage_request = Storage.objects.get(pk=storage_id)
    return render(request, '../templates/storage.html', {'table': storage_request})







