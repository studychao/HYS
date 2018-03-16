# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import UserInfo,KeyWordsInfo

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','mail','create_time']

class KeyWordsInfoAdmin(admin.ModelAdmin):
	list_display = ['id','kw_name','create_time']


admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(KeyWordsInfo,KeyWordsInfoAdmin)
