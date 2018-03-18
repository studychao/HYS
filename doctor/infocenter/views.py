from datetime import date
from django.shortcuts import render,redirect
from infocenter.models import News,Document

# 查询所有图书并显示的视图函数
def index(request):
    news=News.objects.all()
    document=Document.objects.all()
    return render(request,'infocenter.html',{'news':news,'document':document})

