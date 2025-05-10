# Weather Conditions Model
from django.db import models
class WeatherCondition(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    condition = models.CharField(max_length=100)
