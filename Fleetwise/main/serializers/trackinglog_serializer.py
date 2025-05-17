from rest_framework import serializers
from .models import TrackingLog

class TrackingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingLog
        fields = '__all__'
