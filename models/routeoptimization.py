from django.db import models

class RouteOptimization(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    optimized_route = models.TextField()

    def __str__(self):
        return f"Route from {self.start_location} to {self.end_location}"
