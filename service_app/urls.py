from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from service_app import views

urlpatterns = [
    url(r'^floors/$', views.FloorList.as_view()),
    url(r'^floors/(?P<pk>[0-9]+)/$', views.FloorDetail.as_view()),
    url(r'^groups/$', views.GroupList.as_view()),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
    url(r'^wards/$', views.WardList.as_view()),
    url(r'^wards/(?P<pk>[0-9]+)/$', views.WardDetail.as_view()),
    url(r'^boxes/$', views.BoxList.as_view()),
    url(r'^boxes/(?P<pk>[0-9]+)/$', views.BoxDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
