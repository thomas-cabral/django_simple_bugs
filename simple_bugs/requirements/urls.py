from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^$', views.RequirementList.as_view(), name='requirement_list'),
    url(r'^create/$', views.RequirementCreate.as_view(), name='requirement_create'),
    url(r'^(?P<pk>\d+)/(?P<slug>[0-9A-Za-z-_.//]+)/update/$',
        views.RequirementUpdate.as_view(), name='requirement_update'),
    url(r'^(?P<pk>\d+)/(?P<slug>[0-9A-Za-z-_.//]+)/cases/$',
        views.RequirementCases.as_view(), name='requirement_cases'),
    url(r'^(?P<pk>\d+)/(?P<slug>[0-9A-Za-z-_.//]+)/$',
        views.RequirementDetail.as_view(), name='requirement_detail'),
)