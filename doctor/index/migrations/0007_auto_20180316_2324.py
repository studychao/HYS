# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180316_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keywordsinfo',
            old_name='name',
            new_name='kw_name',
        ),
    ]
