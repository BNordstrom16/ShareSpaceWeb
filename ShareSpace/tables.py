import django_tables2 as tables
from django_tables2 import A
from .models import Storage


class StorageTable(tables.Table):
    details = tables.LinkColumn("storage", kwargs={"storage_id": A("pk")}, empty_values=(), text='Details')
    user_id = tables.Column(verbose_name='Owner')

    class Meta:
        model = Storage
        attrs = {'class': 'table'}

