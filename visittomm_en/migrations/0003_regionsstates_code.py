# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visittomm_en', '0002_auto_20160420_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionsstates',
            name='code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
