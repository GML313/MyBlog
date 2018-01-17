from django.conf.urls import *
from django.contrib import admin

from . import views,tests

app_name = 'myblog'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^tag(?P<tag>\w+)/$',views.search_tag,name='search_tag'),
    url(r'^archives/$',views.archives,name='archives'),
    url(r'^search/$',views.blog_search,name='search'),
]