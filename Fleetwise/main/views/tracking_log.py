from rest_framework.viewsets import ModelViewSet
from .models import TrackingLog
from .serializers import trackingLogSerializer
from .permissions import IsAdminOrReadOnlyExceptRestricted

class TrackingLogViewSet(ModelViewSet):
    queryset = TrackingLog.objects.all()
    serializer_class = TrackingLogSerializer
    permission_classes = [IsAdminOrReadOnlyExceptRestricted]
