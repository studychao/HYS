# -*- coding:utf-8 -*-

from django.contrib import admin
# Register your models here.

from infocenter.models import Document,News

admin.site.register(Document)
admin.site.register(News)
