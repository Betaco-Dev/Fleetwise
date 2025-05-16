from rest_framework.viewsets import ModelViewSet
from .models import AnalyticsReport
from .serializers import AnalyticsReportSerializer

class AnalyticsReportViewSet(ModelViewSet):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
