from django.db import models
from django.core.exceptions import ValidationError
from .user import User
from .vehicle import Vehicle

class RoutePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Ensure start_date is not after end_date
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be later than end date.")

    def __str__(self):
        return f"Route Plan {self.id} - {self.user.name} ({self.start_date} to {self.end_date})"
