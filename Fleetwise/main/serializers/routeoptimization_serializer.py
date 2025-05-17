from rest_framework import serializers
from .models import (RouteOptimization)

class RouteOptimizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteOptimization
        fields = '__all__'
