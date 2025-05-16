from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, Spectacular
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    AdminViewSet, UsersViewSet, VehicleViewSet, TrackingLogViewSet,
    MaintenanceScheduleViewSet, FuelExpenseViewSet, RouteOptimizationViewSet,
    RoutePlanViewSet, OtherExpenseViewSet, DeliveryUpdateViewSet,
    AnalyticsReportViewSet, CurrencyViewSet, AuditLogViewSet,
    PredictionViewSet, WeatherConditionViewSet, UserPreferenceViewSet,
    FleetAlertViewSet
)
from .custom_views import RateLimitedLoginView, predict_maintenance_view, detect_anomalies_view

# DRF Router for API Endpoints
router = DefaultRouter()
router.register('admin', AdminViewSet)
router.register('users', UsersViewSet)
router.register('vehicles', VehiclesViewSet)
router.register('tracking-logs', TrackingLogsViewSet)
router.register('maintenanceschedule', MaintenanceScheduleViewSet)
router.register('fuel-expenses', FuelExpensesViewSet)
router.register('route-optimization', RouteOptimizationViewSet)
router.register('route-plan', RoutePlanViewSet)
router.register('other-expenses', OtherExpensesViewSet)
router.register('delivery-updates', DeliveryUpdatesViewSet)
router.register('analytics-report', AnalyticsReportViewSet)
router.register('currency', CurrencyViewSet)
router.register('audit-logs', AuditLogsViewSet)
router.register('ai-prediction', PredictionViewSet)
router.register('weather-conditions', WeatherConditionsViewSet)
router.register('user-preference', UserPreferenceViewSet)
router.register('fleet-alert', FleetAlertViewSet)
router.register('ai-maintenance', MaintenancePredictionViewSet)

# URL Patterns
urlpatterns = [
    # API Endpoints
    path('api/', include(router.urls)),

    # Custom Views
    path('login/', RateLimitedLoginView.as_view(), name='login'),
    path('predict-maintenance/', predict_maintenance_view, name='predict_maintenance'),
    path('detect-anomalies/', detect_anomalies_view, name='detect_anomalies'),
    path('custom/', include('Fleetwise.custom_urls')),
     # API Endpoints
    path('api/v1/', include(('fleet.api_urls', 'api'), namespace='api')),

    # API documentation
    path('api/schema', SpectacularAPIView.as_View(), name='schema')  
    path('api/docs', SpectacularSWAGGERView.as_View(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc UI 
     path('api/v1/', include(('fleet.api_urls', 'api'), namespace='api')),
    path('', include(('fleet.custom_urls', 'custom'), namespace='custom')),

    # Token Authentication
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
from django.conf.urls import handler404, handler500
from .views import custom_404_view, custom_500_view

handler404 = 'fleet.views.custom_404_view'
handler500 = 'fleet.views.custom_500_view'
