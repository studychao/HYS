# -*- coding:utf-8 -*-

from django.db import models

class News(models.Model):
    # 图书名称，唯一
    Ntitle = models.CharField(max_length=50, unique=True)
    Npub_date = models.DateField()

# 定义英雄模型类HeroInfo
class Document(models.Model):
    Dtitle = models.CharField(max_length=50, unique=True)
    Dpub_date = models.CharField(max_length=50)
