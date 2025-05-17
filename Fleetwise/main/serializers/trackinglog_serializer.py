from rest_framework import TrackingLog
from .models import TrackingLog

class TrackingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingLog
        fields = '__all__'
