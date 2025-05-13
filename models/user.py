from django.contrib.auth.models import AbstractUser
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class User(AbstractUser):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = EncryptedCharField(max_length=15, blank=True, null=True, validators=[phone_validator])
    
    role = models.CharField(
        max_length=10,
        choices=[
            ('Driver', _('Driver')),
            ('Rider', _('Rider')),
        ],
        default='Driver'
    )
    license_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.role == 'Driver', 'Rider'and not self.license_number:
            raise ValidationError("License number is required for drivers.")

    def __str__(self):
        return self.username

    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['role']),
        ]
