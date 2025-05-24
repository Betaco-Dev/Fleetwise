from Fleetwise.main import models
from django.utils.timezone import now
from .user import User
from .vehicle import Vehicle

class DeliveryUpdate(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    update_timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Delivery Update {self.id} - {self.user.name} ({self.status})"

    def update_status(self, new_status):
        """ Update the delivery status and timestamp """
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.update_timestamp = now()
            self.save()
        else:
            raise ValueError("Invalid status provided.")

    @classmethod
    def get_updates_for_user(cls, user):
        """ Retrieve all updates for a specific user """
        return cls.objects.filter(user=user).order_by('-update_timestamp')
