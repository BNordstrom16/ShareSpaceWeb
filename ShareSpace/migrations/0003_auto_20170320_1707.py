# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShareSpace', '0002_storage_storage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='storage_name',
            field=models.CharField(default='Storage', max_length=40),
        ),
    ]
