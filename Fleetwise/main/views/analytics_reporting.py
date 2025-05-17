from rest_framework.viewsets import ModelViewSet
from .models import AnalyticsReport
from .serializers import AnalyticsReportSerializer
from .permissions import IsAdminOrReadOnlyExceptRestricted

class AnalyticsReportViewSet(ModelViewSet):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
    permission_classes  = [IsAdminOrReadOnlyExceptRestricted]
