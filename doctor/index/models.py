# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    #id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    create_time = models.DateField()#auto_now_add=True
    #逻辑删除，默认不删除
    idDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class KeyWordsInfo(models.Model):
	#id = models.IntegerField(unique=True)
	kw_name = models.CharField(max_length=50,unique=True)
	create_time = models.DateField()#auto_now_add=True
	idDelete = models.BooleanField(default=False)


