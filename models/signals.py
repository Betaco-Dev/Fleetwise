from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, AuditLog

@receiver(post_save, sender=User)
def log_user_save(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"
    AuditLog.objects.create(user=instance, action=f"{action} user {instance.username}")

@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    AuditLog.objects.create(user=instance, action=f"Deleted user {instance.username}")
