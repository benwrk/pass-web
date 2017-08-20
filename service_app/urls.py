from django.conf.urls import url
from service_app import views

urlpatterns = [
    url(r'^floors/$', views.floor_list),
    url(r'^floors/(?P<pk>[0-9]+)/$', views.floor_detail),
]
