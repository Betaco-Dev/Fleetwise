from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet  # change this to match your ViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # adjust 'users' and 'user' as needed

urlpatterns = [
    path('', include(router.urls)),
]
