from rest_framework.viewsets import ModelViewSet
from .models import UserPreferences
from .serializers import UserPreferenceSerializer

class UserPreferenceViewSet(ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
