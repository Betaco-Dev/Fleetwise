from rest_framework.viewsets import ModelViewSet
from .models import DeliveryUpdates
from .serializers import DeliveryUpdatesSerializer

class DeliveryUpdatesViewSet(ModelViewSet):
    queryset = DeliveryUpdates.objects.all()
    serializer_class = DeliveryUpdatesSerializer
