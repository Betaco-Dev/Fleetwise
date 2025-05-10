from django.db import models
from .user import User

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=10, choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Light')
    notifications_enabled = models.BooleanField(default=True)
