__author__ = 'Thomas'
from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^bugs/$', views.BugList.as_view(), name='bug_list'),
    url(r'^bugs/(?P<pk>\d+)/$', views.BugDetail.as_view(), name='bug_detail',),
    url(r'^bugs/create/$', views.BugCreate.as_view(), name='bug_create'),
    url(r'^requirement/$', views.RequirementList.as_view(), name='requirement_list'),
    url(r'^requirement/(?P<pk>\d+)/$', views.RequirementDetail.as_view(), name='requirement_detail'),
    )