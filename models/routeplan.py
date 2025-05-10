from django.db import models
from .user import User
from .vehicle import Vehicle

class RoutePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Route Plan {self.id} - {self.user.name}"
