# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('登陆成功')
            else:
                return HttpResponse('登陆失败')
        else:
            return HttpResponse('登陆失败')

    else:
        form = LoginForm()
    return render(request,'sign-in.html',{'form': form})



@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard'})
