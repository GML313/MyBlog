# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,blank=True)
    data_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)
    def __unicode__(self): #方便在数据库中存放中文标题
        return self.title
    class Meta:
        ordering = ['-data_time']