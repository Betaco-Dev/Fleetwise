from rest_framework.viewsets import ModelViewSet
from .models import FuelExpense
from .serializers import FuelExpenseSerializer

class FuelExpenseViewSet(ModelViewSet):
    queryset = FuelExpense.objects.all()
    serializer_class = FuelExpenseSerializer
