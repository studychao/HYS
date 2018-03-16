# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from index.models import UserInfo
# Create your views here.

def addUser(request):
	user=UserInfo()
	#user.id=10000
	user.name='测试'
	user.mail='测试'
	user.save()
	return redirect('/index/')


def index(request):
    return render(request,'index.html')

def sign_in(request):
    return render(request,'sign-in.html')

def sign_up(request):
    return render(request,'sign-up.html')
