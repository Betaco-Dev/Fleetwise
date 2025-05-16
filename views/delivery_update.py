from rest_framework.viewsets import ModelViewSet
from .models import DeliveryUpdate
from .serializers import DeliveryUpdateSerializer

class DeliveryUpdatesViewSet(ModelViewSet):
    queryset = DeliveryUpdate.objects.all()
    serializer_class = DeliveryUpdateSerializer
