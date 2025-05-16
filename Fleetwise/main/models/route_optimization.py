from django.db import models
from django.core.exceptions import ValidationError

class RouteOptimization(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    optimized_route = models.TEXTField()  # Use 
    distance = models.FloatField(null=True, blank=True, help_text="Distance in kilometers")
    duration = models.FloatField(null=True, blank=True, help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.start_location == self.end_location:
            raise ValidationError("Start and end locations cannot be the same.")

    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location}"
