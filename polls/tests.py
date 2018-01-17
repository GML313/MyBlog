# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.http import HttpResponse

from polls.models import Question,Choice,UserInfo

def testdb(request):
    response = ""
    response1 = ""
    lst = Question.objects.all()
    response2 = Question.objects.filter(id=1)
    response3 = Question.objects.get(id=1)
    return HttpResponse("<p>" + response2 + "</p>")
