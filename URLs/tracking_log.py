from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackingLogViewSet

router = DefaultRouter()
router.register(r'tracking-log', TrackingLogViewSet, basename='tracking_log')

urlpatterns = [
    path('', include(router.urls)),
]
