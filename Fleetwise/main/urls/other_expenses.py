from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OtherExpenseViewSet

router = DefaultRouter()
router.register(r'other-expense', OtherExpensesViewSet, basename='other_expense')

urlpatterns = [
    path('', include(router.urls)),
]
