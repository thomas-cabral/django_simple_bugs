from . import views

__author__ = 'Thomas'
from django.conf.urls import patterns, url
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
                       url(r'^$', views.Index.as_view(), name='index'),

                       url(r'^api/cases/$', views.CaseList.as_view()),
                       url(r'^api/cases/(?P<pk>\d+)', views.CaseDetail.as_view()),

                       url(r'^api/requirements/$', views.RequirementList.as_view()),

                       url(r'^api/projects/$', views.ProjectList.as_view()),

                       url(r'^angular/pages/list/$', TemplateView.as_view(
                           template_name='simple_bugs/angular_templates/list.html')),

                       url(r'^angular/pages/detail/$', TemplateView.as_view(
                           template_name='simple_bugs/angular_templates/detail.html')),

)