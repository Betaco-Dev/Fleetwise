from rest_framework.viewsets import ModelViewSet
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport,
    Currency, AuditLog, Prediction, WeatherCondition, UserPreference, FleetAlert
)
from .serializers import (
    AdminSerializer, UserSerializer, VehicleSerializer, TrackingLogSerializer,
    MaintenanceScheduleSerializer, FuelExpenseSerializer, RouteOptimizationSerializer,
    RoutePlanSerializer, OtherExpenseSerializer, DeliveryUpdateSerializer,
    AnalyticsReportSerializer, CurrencySerializer, AuditLogSerializer,
    PredictionSerializer, WeatherConditionSerializer, UserPreferenceSerializer,
    FleetAlertSerializer
)

# DRF ViewSets for CRUD Operations

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class TrackingLogViewSet(ModelViewSet):
    queryset = TrackingLog.objects.all()
    serializer_class = TrackingLogSerializer

class MaintenanceScheduleViewSet(ModelViewSet):
    queryset = MaintenanceSchedule.objects.all()
    serializer_class = MaintenanceScheduleSerializer

class FuelExpenseViewSet(ModelViewSet):
    queryset = FuelExpense.objects.all()
    serializer_class = FuelExpenseSerializer

class RouteOptimizationViewSet(ModelViewSet):
    queryset = RouteOptimization.objects.all()
    serializer_class = RouteOptimizationSerializer

class RoutePlanViewSet(ModelViewSet):
    queryset = RoutePlan.objects.all()
    serializer_class = RoutePlanSerializer

class OtherExpenseViewSet(ModelViewSet):
    queryset = OtherExpense.objects.all()
    serializer_class = OtherExpenseSerializer

class DeliveryUpdateViewSet(ModelViewSet):
    queryset = DeliveryUpdate.objects.all()
    serializer_class = DeliveryUpdateSerializer

class AnalyticsReportViewSet(ModelViewSet):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer

class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class AuditLogViewSet(ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

class PredictionViewSet(ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

class WeatherConditionViewSet(ModelViewSet):
    queryset = WeatherCondition.objects.all()
    serializer_class = WeatherConditionSerializer

class UserPreferenceViewSet(ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

class FleetAlertViewSet(ModelViewSet):
    queryset = FleetAlert.objects.all()
    serializer_class = FleetAlertSerializer
