# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180316_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWordsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_id', models.IntegerField(unique=True)),
                ('keyword_name', models.CharField(max_length=50, unique=True)),
                ('keyword_create_time', models.DateField()),
                ('idDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='add_time',
            new_name='user_create_time',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='password',
            new_name='user_password',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='mail',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='idDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_mail',
            field=models.CharField(default=0, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
    ]
