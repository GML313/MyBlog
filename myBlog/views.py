# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Article
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def test(request):
    return render(request, 'templates/myBlog/test.html', {'current_time': datetime.now()})
def home(request):
    posts = Article.objects.all()
    print
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request,'templates/myBlog/home.html',{'post_list':post_list})
def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    #print "title = %s, category = %s, date_time = %s, content = %s" %(post.title, post.category, post.data_time, post.content)
    return render(request,'templates/myBlog/post.html',{'post':post})
def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'templates/myBlog/archives.html', {'post_list' : post_list,
                                            'error' : False})
def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'templates/myBlog/tag.html',{'post_list':post_list})
def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'templates/myBlog/home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'templates/myBlog/archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'templates/myBlog/archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')