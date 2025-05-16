from rest_framework.viewsets import ModelViewSet
from .models import OtherExpense
from .serializers import OtherExpenseSerializer

class OtherExpenseViewSet(ModelViewSet):
    queryset = OtherExpense.objects.all()
    serializer_class = OtherExpenseSerializer
