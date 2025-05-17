from rest_framework import serializers
from .models import (DeliveryUpdate)

class DeliveryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryUpdate
        fields = '__all__'
