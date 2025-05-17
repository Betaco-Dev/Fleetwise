from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Fleetwise.main.serializers import TrackingLogSerializer
from Fleetwise.main.services.tracking_log_utils import reconstruct_trip_path
from Fleetwise.main.models.tracking_log import TrackingLog
from Fleetwise.main.models.vehicle import Vehicle
from .api_views import (
    AdminViewSet, UserViewSet, VehicleViewSet, TrackingLogViewSet,
    MaintenanceScheduleViewSet, FuelExpenseViewSet, RouteOptimizationViewSet,
    RoutePlanViewSet, OtherExpenseViewSet, DeliveryUpdateViewSet,
    AnalyticsReportViewSet, CurrencyViewSet, AuditLogViewSet,
    AiPredictionViewSet, WeatherConditionViewSet, UserPreferenceViewSet,
    FleetAlertViewSet, AiMaintenanceViewSet
)

# DRF Router for API Endpoints with versioning
router = DefaultRouter()
router.register('v1/admins', AdminViewSet)
router.register('v1/users', UserViewSet)
router.register('v1/vehicles', VehicleViewSet)
router.register('v1/tracking-logs', TrackingLogViewSet)
router.register('v1/maintenance', MaintenanceScheduleViewSet)
router.register('v1/fuel-expenses', FuelExpenseViewSet)
router.register('v1/route-optimizations', RouteOptimizationViewSet)
router.register('v1/route-plans', RoutePlanViewSet)
router.register('v1/other-expenses', OtherExpenseViewSet)
router.register('v1/delivery-updates', DeliveryUpdateViewSet)
router.register('v1/analytics-reports', AnalyticsReportViewSet)
router.register('v1/currencies', CurrencyViewSet)
router.register('v1/audit-logs', AuditLogViewSet)
router.register('v1/aipredictions', PredictionViewSet)
router.register('v1/weather-conditions', WeatherConditionViewSet)
router.register('v1/user-preferences', UserPreferenceViewSet)
router.register('v1/fleet-alerts', FleetAlertViewSet)
router.register('v1/ai-maintenance', AiMaintenanceViewSet)

# API URL Patterns with namespace
app_name = 'Fleetwise'
urlpatterns = router.urls

#API Tracking log view

class TrackingLogCreateAPIView(APIView):
    def post(self, request):
        serializer = TrackingLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripPathAPIView(APIView):
    def get(self, request, vehicle_id, trip_date):
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        trip_points = reconstruct_trip_path(vehicle, trip_date)
        return Response({'trip_points': trip_points}
