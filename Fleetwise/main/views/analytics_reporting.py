from rest_framework.viewsets import ModelViewSet
from Fleetwise.main.models import AnalyticsReport
from .serializers import AnalyticsReportSerializer
from .permissions import IsAdminOrReadOnlyExceptRestricted

class AnalyticsReportViewSet(ModelViewSet):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
    permission_classes  = [IsAdminOrReadOnlyExceptRestricted]
    
class AnalyticsReportListView(generics.ListCreateAPIView):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
    permission_classes  = [IsAdminOrReadOnlyExceptRestricted]

class AnalyticsReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
    permission_classes  = [IsAdminOrReadOnlyExceptRestricted]
