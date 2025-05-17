from rest_framework.viewsets import ModelViewSet
from .models import AuditLog
from .serializers import AuditLogSerializer
from .permissions import IsAdminOrReadOnlyExceptRestricted

class AuditLogViewSet(ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminOrReadOnlyExceptRestricted]
