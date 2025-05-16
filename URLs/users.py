from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet  # change this to match your ViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')  # adjust 'users' and 'user' as needed

urlpatterns = [
    path('', include(router.urls)),
]
