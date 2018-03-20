# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    favortopic1 = models.CharField(max_length=50)
    favortopic2 = models.CharField(max_length=50)
    favortopic3 = models.CharField(max_length=50)

def __str__(self):
    return 'Profile for user {}'.format(self.user.username)
