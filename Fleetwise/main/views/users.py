from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersSerializer

class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
