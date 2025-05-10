from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password_hash = models.CharField(max_length=255)  # Use Django's built-in hashing

    def __str__(self):
        return self.name
