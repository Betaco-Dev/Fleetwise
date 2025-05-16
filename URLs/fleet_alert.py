from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FleetAlertViewSet

router = DefaultRouter()
router.register(r'fleet-alerts', FleetAlertViewSet, basename='fleetalert')

urlpatterns = [
    path('', include(router.urls)),
]
