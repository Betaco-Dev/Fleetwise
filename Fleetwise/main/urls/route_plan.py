from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutePlanViewSet

router = DefaultRouter()
router.register(r'route-plan', RoutePlanViewSet, basename='route_plan')

urlpatterns = [
    path('', include(router.urls)),
]
