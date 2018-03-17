# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.

'''class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #image = models.ImageField(upload_to='static/image/%Y/%m', default='static/image/default.jpg', max_length=200,
                            #  blank=True, null=True, verbose_name='用户头像')
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username'''

'''class UserInfo(models.Model):
    #id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    create_time = models.DateField()#auto_now_add=True
    #逻辑删除，默认不删除
    idDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name'''

'''class KeyWordsInfo(models.Model):
	#id = models.IntegerField(unique=True)
	name = models.CharField(max_length=50,unique=True)
	create_time = models.DateField()#auto_now_add=True
	idDelete = models.BooleanField(default=False)'''


