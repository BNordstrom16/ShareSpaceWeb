import django_tables2 as tables
from .models import Storage


class StorageTable(tables.Table):

    class Meta:
        model = Storage
        attrs = {'class': 'table'}
