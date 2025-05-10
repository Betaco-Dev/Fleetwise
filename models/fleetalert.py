from django.db import models
from .user import User
from .vehicle import Vehicle

class FleetAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    alert_type = models.CharField(max_length=50)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
