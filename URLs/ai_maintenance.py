from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AiMaintenanceViewSet

router = DefaultRouter()
router.register(r'ai-maintenance', PredictionViewSet, basename='ai_maintenance')

urlpatterns = [
    path('', include(router.urls)),
]
