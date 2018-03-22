# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import Profile

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


class ProfileEditForm(forms.Form):
    favortopic1 = forms.ChoiceField(choices=[(u'鼻炎','鼻炎'),(u'肺癌','肺癌')],label='选择专业领域1')
    favortopic2 = forms.ChoiceField(choices=[(u'鼻炎','鼻炎'),(u'肺癌','肺癌')],label='选择专业领域2')

#class Meta:
#    model = Profile
#       fields = ('favortopic1','favortopic2')

