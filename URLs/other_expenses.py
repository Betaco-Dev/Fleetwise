from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OtherExpensesViewSet

router = DefaultRouter()
router.register(r'other-expense', OtherExpensesViewSet, basename='otherexpense')

urlpatterns = [
    path('', include(router.urls)),
]
