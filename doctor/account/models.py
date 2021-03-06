# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    favortopic1 = models.CharField(max_length=50)
    favortopic2 = models.CharField(max_length=50)
    favor_id=models.CharField(max_length=50,default="")

class Collection(models.Model):
    user_id=models.CharField(max_length=50,default="")
    document_id=models.CharField(max_length=50,default="")

def __str__(self):
    return 'Profile2 for user {}'.format(self.user.username)


class Document(models.Model):
    Dtitle = models.CharField(max_length=50, unique=True)
    Dkeyword = models.CharField(max_length=50)
    Dauther = models.CharField(max_length=150)
    Dsummary = models.CharField(max_length=256)
    Dshoulu_date = models.CharField(max_length=50)
    Dpub_date = models.DateField()
    Durl = models.CharField(max_length=100)

