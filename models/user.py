from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('Driver', 'Driver'),
        ('Rider', 'Rider'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Rider')
    license_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
