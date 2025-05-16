from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryUpdatesViewSet

router = DefaultRouter()
router.register(r'delivery-update', DeliveryUpdatesViewSet, basename='deliveryupdates')

urlpatterns = [
    path('', include(router.urls)),
]
