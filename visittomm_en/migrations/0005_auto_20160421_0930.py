# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visittomm_en', '0004_auto_20160421_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='cities',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='regionsstates',
            old_name='name',
            new_name='title',
        ),
    ]
