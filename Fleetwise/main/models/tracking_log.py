from django.db import models
from django.core.exceptions import ValidationError
from .user import Users
from .vehicle import Vehicle

class TrackingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    date_time = models.DateTimeField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Validate latitude and longitude ranges
        if not (-90 <= self.latitude <= 90):
            raise ValidationError("Latitude must be between -90 and 90.")
        if not (-180 <= self.longitude <= 180):
            raise ValidationError("Longitude must be between -180 and 180.")

    def __str__(self):
        return f"Log {self.id} - {self.user.name} at {self.date_time}"

    class Meta:
        indexes = [
            models.Index(fields=["date_time"]),
            models.Index(fields=["latitude", "longitude"]),
        ]
