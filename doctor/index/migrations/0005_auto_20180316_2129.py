# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180316_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordsinfo',
            name='create_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
