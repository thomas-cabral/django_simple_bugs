__author__ = 'Thomas'
from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^cases/$', views.CaseList.as_view(), name='case_list'),
    url(r'^cases/(?P<pk>\d+)/update/$', views.CaseUpdate.as_view(), name='case_update'),
    url(r'^cases/(?P<pk>\d+)/$', views.CaseDetail.as_view(), name='case_detail',),
    url(r'^cases/create/$', views.CaseCreate.as_view(), name='case_create'),
    url(r'^requirement/$', views.RequirementList.as_view(), name='requirement_list'),
    url(r'^requirement/create/$', views.RequirementCreate.as_view(), name='requirement_create'),
    url(r'^requirement/(?P<pk>\d+)/update/$', views.RequirementUpdate.as_view(), name='requirement_update'),
    url(r'^requirement/(?P<pk>\d+)/$', views.RequirementDetail.as_view(), name='requirement_detail'),
    url(r'^requirement/(?P<pk>\d+)/cases/$', views.RequirementCases.as_view(), name='requirement_cases'),
    url(r'^profile/(?P<username>\w+)/$', views.Profile.as_view(), name='profile'),
    )