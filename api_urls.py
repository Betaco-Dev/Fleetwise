from rest_framework.routers import DefaultRouter
from .api_views import (
    AdminViewSet, UserViewSet, VehicleViewSet, TrackingLogViewSet,
    MaintenanceScheduleViewSet, FuelExpenseViewSet, RouteOptimizationViewSet,
    RoutePlanViewSet, OtherExpenseViewSet, DeliveryUpdateViewSet,
    AnalyticsReportViewSet, CurrencyViewSet, AuditLogViewSet,
    PredictionViewSet, WeatherConditionViewSet, UserPreferenceViewSet,
    FleetAlertViewSet
)

# DRF Router for API Endpoints
router = DefaultRouter()
router.register('admins', AdminViewSet)
router.register('users', UserViewSet)
router.register('vehicles', VehicleViewSet)
router.register('tracking-logs', TrackingLogViewSet)
router.register('maintenance', MaintenanceScheduleViewSet)
router.register('fuel-expenses', FuelExpenseViewSet)
router.register('route-optimizations', RouteOptimizationViewSet)
router.register('route-plans', RoutePlanViewSet)
router.register('other-expenses', OtherExpenseViewSet)
router.register('delivery-updates', DeliveryUpdateViewSet)
router.register('analytics-reports', AnalyticsReportViewSet)
router.register('currencies', CurrencyViewSet)
router.register('audit-logs', AuditLogViewSet)
router.register('predictions', PredictionViewSet)
router.register('weather-conditions', WeatherConditionViewSet)
router.register('user-preferences', UserPreferenceViewSet)
router.register('fleet-alerts', FleetAlertViewSet)

# API URL Patterns
urlpatterns = router.urls
