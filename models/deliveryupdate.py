from django.db import models
from .user import User
from .vehicle import Vehicle

class DeliveryUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100)
    update_timestamp = models.DateTimeField()

    def __str__(self):
        return f"Delivery Update {self.id} - {self.user.name}"
