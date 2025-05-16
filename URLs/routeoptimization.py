from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteOptimizationViewSet

router = DefaultRouter()
router.register(r'route-optimization', RouteOptimizationViewSet, basename='routeoptimization')

urlpatterns = [
    path('', include(router.urls)),
]
