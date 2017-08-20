from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from service_app import views

urlpatterns = [
    url(r'^floors/$', views.FloorList.as_view()),
    url(r'^floors/(?P<pk>[0-9]+)/$', views.FloorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
