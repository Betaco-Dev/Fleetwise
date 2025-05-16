from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutePlanViewSet

router = DefaultRouter()
router.register(r'route-plan', RoutePlanViewSet, basename='routeplan')

urlpatterns = [
    path('', include(router.urls)),
]
