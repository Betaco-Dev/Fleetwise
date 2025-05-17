from rest_framework import serializers
from Fleetwise.main.models.route_plan import RoutePlan

class RoutePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutePlan
        fields = [
            'id', 'user', 'vehicle', 'start_date', 'end_date',
            'description', 'created_at', 'updated_at'
        ]
