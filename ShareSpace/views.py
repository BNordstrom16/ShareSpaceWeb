from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from .models import Storage
from django_tables2 import RequestConfig
from .tables import StorageTable
from django.contrib.auth.decorators import login_required
from .forms import StorageForm, QuestionForm


def index(request):
    table = Storage.objects.reverse()[0:3]
    return render(request, '../templates/index.html', {'storages': table})


def about(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return '/about'
    else:
        form = QuestionForm()

    return render(request, '../templates/about.html', {'form': form})


def current_storages(request):
    table = StorageTable(Storage.objects.all())
    RequestConfig(request).configure(table)
    return render(request, '../templates/current_storages.html', {'table': table})

@login_required(login_url='/accounts/login')
def create_storage(request):
    if request.method == "POST":
        form = StorageForm(request.POST, request.FILES)
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
    return render(request, '../templates/storage.html', {'storage': storage_request})


class EditStorage(UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = 'storage_update_form.html'
    success_url = '/current_storages'


class DeleteStorage(DeleteView):
    model = Storage
    template_name = 'storage_confirm_delete.html'
    success_url = '/current_storages'


def show_image(request, storage_id):
    photo_request = Storage.objects.get(pk=storage_id)
    return render(request, '../templates/show_image.html', {'storage': photo_request})







