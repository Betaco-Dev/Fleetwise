from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditLogViewSet

router = DefaultRouter()
router.register(r'audit-log', AuditLogViewSet, basename='auditlog')

urlpatterns = [
    path('', include(router.urls)),
]
