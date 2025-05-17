from rest_framework import serializers
from .models import (RoutePlan)

class RoutePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutePlan
        fields = '__all__'
