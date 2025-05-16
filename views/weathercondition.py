from rest_framework.viewsets import ModelViewSet
from .models import WeatherCondition
from .serializers import WeatherConditionSerializer

class WeatherConditionViewSet(ModelViewSet):
    queryset = WeatherCondition.objects.all()
    serializer_class = WeatherConditionSerializer
