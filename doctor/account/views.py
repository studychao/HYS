# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile,News,Document
from django.contrib import messages
import wan
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

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,'register_done.html',{'new_user':new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request,'register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'成功！')
        else:
            messages.error(request,'失败!')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,'edit.html',{'profile_form':profile_form})

@login_required
def infocenter(request):
    now_user=Profile.objects.get(user_id=request.user.id)
    if(now_user.favortopic1!="NULL"):
        document1=Document.objects.filter(Dkeyword=now_user.favortopic1)
        if(now_user.favortopic2!="NULL"):
            document2=Document.objects.filter(Dkeyword=now_user.favortopic2)
        else:
            pass
    elif(now_user.favortopic2!="NULL"):
        document1=Document.objects.filter(Dkeyword=now_user.favortopic2)
    else:
        pass
    
    return render(request,'infocenter.html',{'news':document1,'document':document2})
