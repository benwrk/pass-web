from django.conf.urls import url, include
from service_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'floors', views.FloorViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'wards', views.WardViewSet)
router.register(r'boxes', views.BoxViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
