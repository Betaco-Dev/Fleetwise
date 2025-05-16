from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuelExpenseViewSet

router = DefaultRouter()
router.register(r'fuel-expense', FuelExpenseViewSet, basename='fuelexpense')

urlpatterns = [
    path('', include(router.urls)),
]
