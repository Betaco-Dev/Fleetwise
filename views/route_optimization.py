from rest_framework.viewsets import ModelViewSet
from .models import RouteOptimization
from .serializers import RouteOptimizationSerializer

class RouteOptimizationViewSet(ModelViewSet):
    queryset = RouteOptimization.objects.all()
    serializer_class = RouteOptimizationSerializer
