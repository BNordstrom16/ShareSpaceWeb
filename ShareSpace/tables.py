import django_tables2 as tables
from django_tables2 import A
from .models import Storage


class StorageTable(tables.Table):
    details = tables.LinkColumn("storage", kwargs={"storage_id": A("pk")}, empty_values=(), text='Details')
    user_id = tables.Column(verbose_name='Owner')
    price = tables.Column(verbose_name='Price Per Month ($)')

    class Meta:
        model = Storage
        exclude = ['photos', 'storage_id']
        attrs = {'class': 'table'}