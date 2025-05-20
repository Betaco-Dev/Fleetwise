from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_optimized_route_view, create_tracking_log, show_trip_path, create_route_plan
from .api_views import (
    AdminViewSet, UserViewSet, VehicleViewSet, TrackingLogViewSet,
    MaintenanceScheduleViewSet, FuelExpenseViewSet, RouteOptimizationViewSet,
    RoutePlanViewSet, OtherExpenseViewSet, DeliveryUpdateViewSet,
    AnalyticsReportViewSet, CurrencyViewSet, AuditLogViewSet,
    PredictionViewSet, WeatherConditionViewSet, UserPreferenceViewSet,
    FleetAlertViewSet, AiMaintenanceViewSet, RouteUtilsViewSet
)
from .custom_views import RateLimitedLoginView, predict_maintenance_view, detect_anomalies_view
from Fleetwise.main.api_views import TrackingLogCreateAPIView, TripPathAPIView, RoutePlanCreateAPIView, OtherExpensesCreateAPIView

# DRF Router for API Endpoints
router = DefaultRouter()
router.register('admin', AdminViewSet)
router.register('users', UserViewSet)
router.register('vehicles', VehicleViewSet)
router.register('tracking-logs', TrackingLogViewSet)
router.register('maintenance-schedule', MaintenanceScheduleViewSet)
router.register('fuel-expenses', FuelExpenseViewSet)
router.register('route-optimization', RouteOptimizationViewSet)
router.register('route-plan', RoutePlanViewSet)
router.register('other-expenses', OtherExpenseViewSet)
router.register('delivery-updates', DeliveryUpdateViewSet)
router.register('analytics-report', AnalyticsReportViewSet)
router.register('currency', CurrencyViewSet)
router.register('audit-logs', AuditLogViewSet)
router.register('ai-prediction', PredictionViewSet)
router.register('weather-conditions', WeatherConditionViewSet)
router.register('user-preference', UserPreferenceViewSet)
router.register('fleet-alert', FleetAlertViewSet)
router.register('ai-maintenance', AiMaintenanceViewSet)
router.register('route-utils', RouteUtilsViewSet)

urlpatterns = [
    # API Endpoints from router
    path('api/', include(router.urls)),

    # Custom tracking log/trip path endpoints
    path('tracking-log/create/', create_tracking_log, name='create_tracking_log'),
    path('tracking-log/trip/<int:vehicle_id>/<str:trip_date>/', show_trip_path, name='show_trip_path'),

    path('api/tracking-log/', TrackingLogCreateAPIView.as_view(), name='api_tracking_log_create'),
    path('api/trip-path/<int:vehicle_id>/<str:trip_date>/', TripPathAPIView.as_view(), name='api_trip_path'),
     path('route-plan/create/', create_route_plan, name='create_route_plan'),
    path('api/route-plan/', RoutePlanCreateAPIView.as_view(), name='api_route_plan_create'),
    path('other-expense/create/', create_other_expense, name='create_route_plan'),
    

    # Custom Views
    path('login/', RateLimitedLoginView.as_view(), name='login'),
    path('predict-maintenance/', predict_maintenance_view, name='predict_maintenance'),
    path('detect-anomalies/', detect_anomalies_view, name='detect_anomalies'),
    path('custom/', include('Fleetwise.custom_urls')),
    path('create-route/', create_optimized_route_view, name='create_optimized_route'),

    # API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Token Authentication
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]

# Custom error handlers
# DO NOT import handler404/handler500—they are not importable symbols!
from .views import custom_404_view, custom_500_view

handler404 = 'fleet.views.custom_404_view'
handler500 = 'fleet.views.custom_500_view'
