# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11 on 2018-03-18 02:06
=======
# Generated by Django 1.11.8 on 2018-03-17 16:24
>>>>>>> 2f11bc308a56839a01616732d534c9c40df764e0
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('email', models.CharField(max_length=30)),
=======
                ('username', models.CharField(max_length=30)),
>>>>>>> 2f11bc308a56839a01616732d534c9c40df764e0
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
