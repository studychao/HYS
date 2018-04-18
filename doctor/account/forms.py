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
    favortopic1 = forms.ChoiceField(choices=[(u'心血管','心血管'),(u'神经','神经'),(u'肿瘤','肿瘤'),(u'消化','消化'),(u'内分泌','内分泌'),(u'呼吸','呼吸'),(u'血液','血液'),(u'感染','感染'),(u'麻醉','麻醉')],label='选择专业领域1')
    favortopic2 = forms.ChoiceField(choices=[(u'心血管','心血管'),(u'神经','神经'),(u'肿瘤','肿瘤'),(u'消化','消化'),(u'内分泌','内分泌'),(u'呼吸','呼吸'),(u'血液','血液'),(u'感染','感染'),(u'麻醉','麻醉')],label='选择专业领域2')

class ProfileEditForm2(forms.Form):
    favortopic1 =forms.CharField(label='输入专业领域1')
    favortopic2 =forms.CharField(label='输入专业领域2')


