import django_tables2 as tables
from .models import Storage


class StorageTable(tables.Table):
    more_info = tables.TemplateColumn('<a href="{% url storage record.id %}">Info</a>')

    class Meta:
        model = Storage
        attrs = {'class': 'table'}
        exclude = 'user_email'

