from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet

router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('', include(router.urls)),
]
