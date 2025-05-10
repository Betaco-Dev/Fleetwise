from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=100,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    password_hash = models.CharField(max_length=255)  # Use Django's built-in hashing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hash the password before saving the model
        if not self.password_hash.startswith('pbkdf2_'):  # Avoid re-hashing an already hashed password
            self.password_hash = make_password(self.password_hash)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
