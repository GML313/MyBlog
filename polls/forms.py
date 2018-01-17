# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms

class ItemForm(forms.Form):
    ItemCode = forms.CharField(max_length=10,label=u'编码号码',error_messages={'required':u'必填项'},)
    ItemName = forms.CharField()
    ItemMobile = forms.CharField()
    ItemTypeChoice = ((0,u'普通用户'),(1, u'高级用户'))
    ItemType = forms.IntegerField(widget=forms.widgets.Select(choices=ItemTypeChoice, attrs={'class':'form-control'}))
    def __str__(self):
        return self.ItemName