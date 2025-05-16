from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserPreferenceViewSet

router = DefaultRouter()
router.register(r'user-preferences', UserPreferenceViewSet, basename='userpreference')

urlpatterns = [
    path('', include(router.urls)),
]
