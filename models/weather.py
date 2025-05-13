from django.db import models
from django.core.exceptions import ValidationError


class WeatherCondition(models.Model):
    CONDITION_CHOICES = [
        ('Sunny', 'Sunny'),
        ('Rainy', 'Rainy'),
        ('Cloudy', 'Cloudy'),
        ('Snowy', 'Snowy'),
        ('Windy', 'Windy'),
        ('Stormy', 'Stormy'),
    ]
    
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)

    def clean(self):
        """
        Custom validation for the WeatherCondition model.
        Ensures temperature is within a realistic range.
        """
        if not (-100 <= self.temperature <= 100):
            raise ValidationError("Temperature must be between -100°C and 100°C.")

    def __str__(self):
        return f"{self.location} on {self.date}: {self.condition}, {self.temperature}°C"

    class Meta:
        indexes = [
            models.Index(fields=['location', 'date']),
        ]
