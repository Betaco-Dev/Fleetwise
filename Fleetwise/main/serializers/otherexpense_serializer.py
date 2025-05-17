from rest_framework import serializers
from .models import (OtherExpense)

class OtherExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherExpense
        fields = '__all__'
