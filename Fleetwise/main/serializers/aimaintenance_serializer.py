from rets_framework import serializers
from .models import (AiMaintenance)

class AiMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiMaintenance
        fields = '__all__'
