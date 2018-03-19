# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='重复密码',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

def clean_password2(self):
    cd = self.cleaned_data
    if cd['password']!=cd['password2']:
        raise forms.ValidationError('Passwords dont match.')
    return cd['password2']
