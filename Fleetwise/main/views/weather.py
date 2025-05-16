from rest_framework.viewsets import ModelViewSet
from .models import Weather
from .serializers import WeatherConditionSerializer

class WeatherConditionViewSet(ModelViewSet):
    queryset = WeatherCondition.objects.all()
    serializer_class = WeatherConditionSerializer
