# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from index.forms import AddForm
#from index.models import UserInfo
# Create your views here.

'''def sign_up(request):
	if request.method == 'POST':

		form = AddForm(request.POST)

		if form.is_valid():
			user = UserInfo()
			user.email = form.cleaned_data['email']
			user.password = form.cleaned_data['password']
			user.save()
			return render(request,'index.html')

	else:
		form = AddForm()
    return render(request,'sign-up.html', {'form':form})'''

'''def addUser(request):
	user=UserInfo()
	#user.id=10000
	#user.name='测试'
	
	#email = request.GET['email']
	#password = request.GET['password']
	user.mail = email
	user.password = password
	user.save()
	return redirect('/index/')'''


def index(request):
    return render(request,'index.html')

'''def sign_in(request):
    return render(request,'sign-in.html')

def sign_up(request):
    return render(request,'sign-up.html')'''
