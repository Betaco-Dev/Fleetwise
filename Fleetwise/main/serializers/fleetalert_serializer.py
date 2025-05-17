from rest_framework import serializers
from .models import (FleetAlert)

class FleetAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetAlert
        fields = '__all__'
