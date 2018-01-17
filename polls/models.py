# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #pub_data = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    tel_num = models.CharField(max_length=11)
    china_id =models.CharField(max_length=16)
    def __str__(self):
        return self.name