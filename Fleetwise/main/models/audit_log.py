from django.db import models
class AuditLog(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ACTION_CHOICES = [
    ('LOGIN', 'Login'),
    ('LOGOUT', 'Logout'),
    ('UPDATE_PROFILE', 'Update Profile'),
    # Add more actions as needed
]
action = models.CharField(max_length=255, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True, db_Index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
@classmethod
def logs_in_date_range(cls, start_date, end_date):
    return cls.objects.filter(timestamp__range=(start_date, end_date))
