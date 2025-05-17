from rest_framework import serializers
from .models import (AiPrediction)

class AiPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiPrediction
        fields = '__all__'
