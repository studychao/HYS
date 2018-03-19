# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
#With django 1.10 I need to pass the callable instead of
#url(r'^login/$', 'django.contrib.auth.views.login', name='login')

from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
urlpatterns = [
               #url(r'^sign_in/$', views.user_login, name='sign_in'),
    url(r'login/$',login, name='login'),
    url(r'logout/$',logout, name='logout'),
    url(r'logout-then-login/$',logout_then_login, name='logout_then_login'),
    url(r'^$',views.dashboard,name='dashboard')
    ]
