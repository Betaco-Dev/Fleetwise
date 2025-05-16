from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackingLogViewSet

router = DefaultRouter()
router.register(r'tracking-logs', TrackingLogViewSet, basename='trackinglog')

urlpatterns = [
    path('', include(router.urls)),
]
