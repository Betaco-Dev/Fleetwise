from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('Vehicle', 'Vehicle'),
        ('Motorcycle', 'Motorcycle'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Vehicle')
    license_plate = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField()

    def clean(self):
        """
        Custom validation for the Vehicle model.
        Ensures the year is within a logical range.
        """
        current_year = now().year
        if self.year < 1886 or self.year > current_year:  # The first automobile was made in 1886
            raise ValidationError("Year must be between 1886 and the current year.")

    def __str__(self):
        return f"{self.type} - {self.license_plate}"

    class Meta:
        ordering = ['year', 'model']
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
