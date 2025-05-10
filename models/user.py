from django.contrib.auth.models import AbstractUser
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class User(AbstractUser):
    phone = EncryptedCharField(max_length=15, blank=True, null=True)
    # Rest of the fields...
    role = models.CharField(
        max_length=10,
        choices=[
            ('Driver', 'Driver'),
            ('Rider', 'Rider'),
        ],
        default='Rider'
    )
    license_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
