from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from service_app import views

router = DefaultRouter()
router.register(r'floors', views.FloorViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'wards', views.WardViewSet)
router.register(r'boxes', views.BoxViewSet)

urlpatterns = [
    url(r'^clients/', include(router.urls)),
    url(r'^schema/$', get_schema_view(title='PASS Web Service')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
