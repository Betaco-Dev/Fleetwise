from rest_framework.viewsets import ModelViewSet
from .models import TrackingLog
from .serializers import trackingLogSerializer

class TrackingLogViewSet(ModelViewSet):
    queryset = TrackingLog.objects.all()
    serializer_class = TrackingLogSerializer
