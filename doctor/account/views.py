# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

class UserForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

def sign_in(request):
    return render_to_response('sign-in.html')

def sign_up(request):
	Method = request.method
	if Method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			try:
				registJudge = User.objects.filter(email=email).get().email
				return render_to_response('sign-in.html',{'registJudge':registJudge})
			except:
				registAdd = User.objects.create(email=email,password=password)
			#registAdd = User.objects.get_or_create(username=username,password=password)[1]
			#if registAdd == False:
				return render_to_response('sign-in.html',{'registAdd':registAdd,'email':email})
	else:
		uf = UserForm()
	return render_to_response('sign-up.html',{'uf':uf,'Method':Method})#,context_instance=RequestContext(req)
   # return render(request,'sign-up.html')
