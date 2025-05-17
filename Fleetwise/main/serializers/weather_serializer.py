from rest_framework import serializers
from .models import (WeatherCondition)

class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCondition
        fields = '__all__'
