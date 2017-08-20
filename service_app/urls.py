from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from service_app import views

urlpatterns = [
    url(r'^floors/$', views.floor_list),
    url(r'^floors/(?P<pk>[0-9]+)/$', views.floor_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
