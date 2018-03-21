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
        profile_form = ProfileEditForm(request.POST)
        if profile_form.is_valid():
            favortopic1 = profile_form.cleaned_data['favortopic1']
            favortopic2 = profile_form.cleaned_data['favortopic2']
            user_id = request.POST['id']
            profile = Profile.objects.get(user_id=int(user_id))
            profile.favortopic1 = favortopic1
            profile.favortopic2 = favortopic2
            profile.save()
            messages.success(request,'成功！请至“账号-数据图书馆”查看您的专业领域文献')
        else:
            messages.error(request,'失败!')
    else:
        profile_form = ProfileEditForm()

    return render(request,'edit.html',{'profile_form':profile_form})

@login_required
def infocenter(request):
<<<<<<< HEAD
    news=News.objects.all()
    document=Document.objects.all()
    return render(request,'infocenter.html',{'news':news,'document':document})

def index(request):
    return render(request,'index.html')

=======
    now_user=Profile.objects.get(user_id=request.user.id)
    if now_user.favortopic1 is not None:
        document1=Document.objects.filter(Dkeyword=now_user.favortopic1)
        if now_user.favortopic2 is not None :
            document2=Document.objects.filter(Dkeyword=now_user.favortopic2)
        else:
            pass
    elif now_user.favortopic2 is not None:
        document1=Document.objects.filter(Dkeyword=now_user.favortopic2)
    else:
        pass
    
    return render(request,'infocenter.html',{'document1':document1,'document2':document2})
>>>>>>> 248d80fdc4a3fef93ef6c2c65abe4896fed4f670
