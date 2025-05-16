from rest_framework.viewsets import ModelViewSet
from .models import Prediction
from .serializers import PredictionSerializer

class PredictionViewSet(ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
