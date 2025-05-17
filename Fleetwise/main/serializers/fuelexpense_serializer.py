from rest_framework import serializers
from .models import (FuelExpense)

class FuelExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelExpense
        fields = '__all__'
