from rest_framework.viewsets import ModelViewSet
from .models import OtherExpenses
from .serializers import OtherExpensesSerializer

class OtherExpensesViewSet(ModelViewSet):
    queryset = OtherExpenses.objects.all()
    serializer_class = OtherExpensesSerializer
