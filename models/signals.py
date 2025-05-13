from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, AuditLog

@receiver(post_save, sender=User)
def log_user_save(sender, instance, created, **kwargs):
    """
    Logs when a user is created or updated.
    """
    try:
        action = "Created" if created else "Updated"
        AuditLog.objects.create(user=instance, action=f"{action} user {instance.username}")
    except Exception as e:
        # Log the error or handle it (e.g., send to an external logging service)
        pass

@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    """
    Logs when a user is deleted.
    """
    try:
        AuditLog.objects.create(user=instance, action=f"Deleted user {instance.username}")
    except Exception as e:
        # Log the error or handle it
        pass
