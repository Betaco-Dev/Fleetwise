from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenanceScheduleViewSet

router = DefaultRouter()
router.register(r'maintenanceschedule', MaintenanceScheduleViewSet, basename='maintenanceschedule')

urlpatterns = [
    path('', include(router.urls)),
]
