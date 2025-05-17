from rest_framework import serializers
from .models import (MaintenanceSchedule)

class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceSchedule
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at'] #Prevent modification of these fields
