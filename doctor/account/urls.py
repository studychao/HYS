# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views as account_views

urlpatterns = [
    url(r'^sign_in/$', account_views.sign_in, name='sign_in'),
    url(r'^sign_up/$', account_views.sign_up, name='sign_up'),
    ]
