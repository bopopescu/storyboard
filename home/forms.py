#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Darcy Liu on 2012-04-12.
Copyright (c) 2012 Close To U. All rights reserved.
"""

from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from models import *

class MinisiteForm(ModelForm):
    class Meta:
        model = Minisite
        fields = ['name','slug']

class PageForm(ModelForm):
    name  = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'input-xxlarge'}))
    slug  = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'input-xxlarge'}))
    text = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'input-xxlarge','rows':10,'cols':''}))
    Format_Choices = (
            ('2', 'markdown'),
        )
    format = forms.ChoiceField(choices=Format_Choices)
    class Meta:
        model = Page
        fields = ['name','slug','text','format']
