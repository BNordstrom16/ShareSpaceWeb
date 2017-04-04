from django import forms

from .models import Storage


class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('storage_name', 'size', 'price', 'area_code')
        exclude = ['user_id']


