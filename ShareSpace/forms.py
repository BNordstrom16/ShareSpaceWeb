import datetime
from django import forms
from django.core.validators import RegexValidator
from .models import Storage


class StorageForm(forms.ModelForm):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
    date_from = forms.DateField(initial=datetime.date.today, help_text='(YYYY-MM-DD)')
    date_to = forms.DateField(initial=datetime.date.today, help_text='(YYYY-MM-DD)')
    area_code = forms.CharField(min_length=5, max_length=5, validators=[numeric])

    class Meta:
        model = Storage
        fields = ('storage_name', 'size', 'price', 'area_code', 'date_from', 'date_to', 'photos')
        exclude = ['user_id']


