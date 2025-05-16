from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsReportingViewSet

router = DefaultRouter()
router.register(r'analytics-reporting', AnalyticsReportingViewSet, basename='analyticsreporting')

urlpatterns = [
    path('', include(router.urls)),
]
