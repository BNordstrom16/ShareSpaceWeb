import datetime

from django import forms

from .models import Storage


class StorageForm(forms.ModelForm):
    date_from = forms.DateField(initial=datetime.date.today, help_text='(YYYY-MM-DD)')
    date_to = forms.DateField(initial=datetime.date.today, help_text='(YYYY-MM-DD)')

    class Meta:
        model = Storage
        fields = ('storage_name', 'size', 'price', 'area_code', 'date_from', 'date_to', 'photos')
        exclude = ['user_id']


