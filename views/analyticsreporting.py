from rest_framework.viewsets import ModelViewSet
from .models import Analytics
from .serializers import AnalyticsSerializer

class AnalyticsViewSet(ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
