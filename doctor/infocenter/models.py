#coding=utf-8
from django.db import models

class News(models.Model):

    Ntitle = models.CharField(max_length=50, unique=True)
    Npub_date = models.DateField()


class Document(models.Model):
    Dtitle = models.CharField(max_length=50, unique=True)
    Dpub_date = models.DateField()
    Durl = models.CharField(max_length=100)

    
