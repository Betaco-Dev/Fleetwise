from rest_framework.viewsets import ModelViewSet
from .models import FuelExpenses
from .serializers import FuelExpensesSerializer

class FuelExpensesViewSet(ModelViewSet):
    queryset = FuelExpenses.objects.all()
    serializer_class = FuelExpensesSerializer
