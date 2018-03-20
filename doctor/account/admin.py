# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile
from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =['user','favortopic1','favortopic2','favortopic3']

admin.site.register(Profile,ProfileAdmin)
