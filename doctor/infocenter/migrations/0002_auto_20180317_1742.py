# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infocenter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='Npub_date',
            new_name='Dpub_date',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='Ntitle',
            new_name='Dtitle',
        ),
    ]
