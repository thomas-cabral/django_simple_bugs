__author__ = 'Thomas'
from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    url(r'^bugs/$', views.BugList.as_view(), name='bug_index'),
    url(r'^requirement/$', views.RequirementList.as_view(), name='requirement_list'),
    url(r'^requirement/(?P<pk>\d+)/$', views.RequirementDetail.as_view(), name='requirement_detail')
    )