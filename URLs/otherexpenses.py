from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OtherExpensesViewSet

router = DefaultRouter()
router.register(r'other-expenses', OtherExpensesViewSet, basename='otherexpenses')

urlpatterns = [
    path('', include(router.urls)),
]
