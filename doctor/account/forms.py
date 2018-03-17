# -*- coding: utf-8 -*-

from django import forms

class AddForm(forms.Form):
    email = forms.IntegerField()
    password = forms.IntegerField()
