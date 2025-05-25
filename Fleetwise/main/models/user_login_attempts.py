from Fleetwise.main.models import models
from django.contrib.auth.models import User

class UserLoginAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    attempt_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"Login Attempt - {self.user} ({self.ip_address}) at {self.attempt_time}"
