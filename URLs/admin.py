from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet  # change this to match your ViewSet

router = DefaultRouter()
router.register(r'admin', AdminViewSet, basename='admin')  # adjust 'users' and 'user' as needed

urlpatterns = [
    path('', include(router.urls)),
]
