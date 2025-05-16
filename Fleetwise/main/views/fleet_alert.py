from rest_framework.viewsets import ModelViewSet
from .models import FleetAlert
from .serializers import FleetAlertSerializer

class FleetAlertViewSet(ModelViewSet):
    queryset = FleetAlert.objects.all()
    serializer_class = FleetAlertSerializer
