from django.conf.urls import *
from django.contrib import admin

from . import views,tests

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/',include(admin.site.urls)),
    #url(r'^$', tests.testdb),
    url(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'(?P<pk>[0-9]+)/results', views.ResultsView.as_view(), name='results'),
    url(r'(?P<question_id>[0-9]+)/vote/', views.vote, name='vote'),
    url(r'^showdb/$', views.showdb, name='showdb'),
    url(r'^form_test/$', views.additem, name="form_test"),
    url(r'^login/$', views.login, name="login"),
    url(r'^home/$', views.home, name="home"),
    url(r'^logout/$', views.logout, name="logout"),
]