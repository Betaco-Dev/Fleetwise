from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenancePredictionViewSet

router = DefaultRouter()
router.register(r'maintenance-prediction', WeatherConditionViewSet, basename='maintenance-prediction')

urlpatterns = [
    path('', include(router.urls)),
]
