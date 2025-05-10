from django.db import models

class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('Vehicle', 'Vehicle'),
        ('Motorcycle', 'Motorcycle'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    license_plate = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField()

    def __str__(self):
        return f"{self.type} - {self.license_plate}"
