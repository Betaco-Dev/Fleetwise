from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator


class User(AbstractUser):
    # Add any custom fields you need
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('Admin', 'Admin'),
            ('Rider', 'Rider'),
            ('Manager', 'Manager'),
        ],
        default='Rider'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
