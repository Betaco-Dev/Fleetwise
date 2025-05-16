from rest_framework.viewsets import ModelViewSet
from .models import MaintenanceSchedule
from .serializers import MaintenanceScheduleSerializer

class MaintenanceScheduleViewSet(ModelViewSet):
    queryset = MaintenanceSchedule.objects.all()
    serializer_class = MaintenanceScheduleSerializer
