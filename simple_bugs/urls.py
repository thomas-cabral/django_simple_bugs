from . import views

__author__ = 'Thomas'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^profile/(?P<username>\w+)/$', views.Profile.as_view(), name='profile'),
    url(r'^api/requirements/$', views.RequirementsApiList.as_view()),
    url(r'^api/requirements/(?P<pk>[0-9]+)/$', views.RequirementsAPIDetail.as_view()),
    url(r'^api/cases/$', views.CaseAPIList.as_view()),
    url(r'^api/cases/(?P<pk>[0-9]+)/$', views.CaseAPIDetail.as_view()),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^socool/$', views.SoCool.as_view(), name='socool'),
    url(r'^socool/pages/list/$', views.List.as_view()),
    url(r'^socool/pages/detail/$', views.Detail.as_view()),
    url(r'^socool/pages/new/$', views.New.as_view()),
    url(r'^socool/pages/search/$', views.Search.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)