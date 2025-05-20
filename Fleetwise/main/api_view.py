from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Fleetwise.main.serializers import (
    TrackingLogSerializer,
    RoutePlanSerializer, OtherExpenseSerializers
)
from Fleetwise.main.services.tracking_log_utils import reconstruct_trip_path
from Fleetwise.main.services.route_plan_utils import check_overlapping_plans
from Fleetwise.main.models.tracking_log import TrackingLog
from Fleetwise.main.models.vehicle import Vehicle
from Fleetwise.main.models.other_expense_utils import create_other_expense
from .api_views import (
    AdminViewSet, UserViewSet, VehicleViewSet, TrackingLogViewSet,
    MaintenanceScheduleViewSet, FuelExpenseViewSet, RouteOptimizationViewSet,
    RoutePlanViewSet, OtherExpenseViewSet, DeliveryUpdateViewSet,
    AnalyticsReportViewSet, CurrencyViewSet, AuditLogViewSet,
    AiPredictionViewSet, WeatherConditionViewSet, UserPreferenceViewSet,
    FleetAlertViewSet, AiMaintenanceViewSet
)


# API Tracking log view
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
        return Response({'trip_points': trip_points})

# API Route plan create view
class RoutePlanCreateAPIView(APIView):
    def post(self, request):
        serializer = RoutePlanSerializer(data=request.data)
        if serializer.is_valid():
            vehicle = serializer.validated_data['vehicle']
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            if check_overlapping_plans(vehicle, start_date, end_date):
                return Response({"detail": "Overlapping route plan exists."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
