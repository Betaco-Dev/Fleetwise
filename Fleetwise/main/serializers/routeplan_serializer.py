from rest_framework import serializers
from Fleetwise.main.models.route_plan import RoutePlan
from .models import (RoutePlan)

class RoutePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutePlan
        fields = '__all__'
