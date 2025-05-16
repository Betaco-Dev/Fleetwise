from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteOptimizationViewSet

router = DefaultRouter()
router.register(r'route-optimization', RouteOptimizationViewSet, basename='route_optimization')

urlpatterns = [
    path('', include(router.urls)),
]
