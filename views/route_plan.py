from rest_framework.viewsets import ModelViewSet
from .models import RoutePlan
from .serializers import RoutePlanSerializer

class RoutePlanViewSet(ModelViewSet):
    queryset = RoutePlan.objects.all()
    serializer_class = RoutePlanSerializer
