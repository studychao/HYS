# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def sign_in(request):
    return render(request,'sign-in.html')

def sign_up(request):
    return render(request,'sign-up.html')
