from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='socool'),
    url(r'^pages/list/$', views.List.as_view()),
    url(r'^pages/detail/$', views.Detail.as_view()),
    url(r'^pages/new/$', views.New.as_view()),
)