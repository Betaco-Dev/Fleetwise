from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
from .models import User, TrackingLog, RouteOptimization
from .serializers import UserSerializer, TrackingLogSerializer, RouteOptimizationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()  # Admin can view all users
        return User.objects.filter(id=self.request.user.id)  # Regular users see only their profile

class TrackingLogViewSet(ModelViewSet):
    serializer_class = TrackingLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return TrackingLog.objects.all()
        return TrackingLog.objects.filter(user=self.request.user)

class RouteOptimizationViewSet(ModelViewSet):
    queryset = RouteOptimization.objects.all()
    serializer_class = RouteOptimizationSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def optimize(self, request):
        # Logic for route optimization
        return Response({"message": "Route optimized successfully"})
