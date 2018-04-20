# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm,ProfileEditForm,ProfileEditForm2
from django.contrib.auth.decorators import login_required
from .models import Profile,Document,Collection
from django.contrib import messages
import wan
import json
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
    list=[]
    list2=[]
    i=0
    now_user=Profile.objects.get(user_id=request.user.id)
    if now_user.favortopic1 == "":
        status = 1#1是新用户
    else:status = 0
    user_info=Collection.objects.filter(user_id=request.user.id)
    if len(user_info)>0:
        for a in user_info:
            document=Document.objects.get(id=a.document_id)
            list.append(document.Dtitle)
            list2.append(document.Durl)
    else:
        i=1
    
    return render(request,'dashboard.html',{'section':'dashboard','status':status,'document':list,'url':list2,'i':i,'List': json.dumps(list2)})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            profile.save()
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
            topic1=Document.objects.filter(Dkeyword=favortopic1)
            topic2=Document.objects.filter(Dkeyword=favortopic2)
            try:
                if topic1[0].Dkeyword is None :
                    pass
            except IndexError,x:
                wan.get_docu(favortopic1)
            try:
                if topic2[0].Dkeyword is None :
                    pass
            except IndexError,x:
                wan.get_docu(favortopic2)
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
    a=1
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
    if request.method=='POST':
        a=request.POST['id']
        collection =Collection(user_id=request.user.id,document_id=a)
        collection.save()
        messages.success(request,'收藏成功！请至“账号-个人中心”查看您的收藏')
    return render(request,'infocenter.html',{'document1':document1,'document2':document2,'keyword1':now_user.favortopic1,'keyword2':now_user.favortopic2})


def index(request):
    return render(request,'index.html')

def production(request):
    return render(request,'production.html')

def aboutus(request):
    return render(request,'aboutus.html')

@login_required
def edit2(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm2(request.POST)
        if profile_form.is_valid():
            favortopic1 = profile_form.cleaned_data['favortopic1']
            favortopic2 = profile_form.cleaned_data['favortopic2']
            topic1=Document.objects.filter(Dkeyword=favortopic1)
            topic2=Document.objects.filter(Dkeyword=favortopic2)
            try:
                if topic1[0].Dkeyword is None :
                    pass
            except IndexError,x:
                wan.get_docu(favortopic1)
            try:
                if topic2[0].Dkeyword is None :
                    pass
            except IndexError,x:
                wan.get_docu(favortopic2)
            user_id = request.POST['id']
            profile = Profile.objects.get(user_id=int(user_id))
            profile.favortopic1 = favortopic1
            profile.favortopic2 = favortopic2
            profile.save()
            messages.success(request,'成功！请至“账号-数据图书馆”查看您的专业领域文献')
        else:
            messages.error(request,'失败!')
    else:
        profile_form = ProfileEditForm2()
    
    return render(request,'edit2.html',{'profile_form':profile_form})
