from rest_framework.viewsets import ModelViewSet
from .models import UserPreference
from .serializers import UserPreferenceSerializer

class UserPreferenceViewSet(ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
