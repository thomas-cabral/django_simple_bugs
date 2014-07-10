from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^$', views.CaseList.as_view(), name='case_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[0-9A-Za-z-_.//]+)/update/$', views.CaseUpdate.as_view(), name='case_update'),
    url(r'^(?P<pk>\d+)/(?P<slug>[0-9A-Za-z-_.//]+)/$', views.CaseDetail.as_view(), name='case_detail',),
    url(r'^create/$', views.CaseCreate.as_view(), name='case_create'),
)