from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .user import User
from django.utils.translation import gettext_lazy as _


class ThemeChoices(models.TextChoices):
    LIGHT = 'Light', 'Light'
    DARK = 'Dark', 'Dark'

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(
        max_length=10,
        choices=ThemeChoices.choices,
        default=ThemeChoices.LIGHT
    )
    notifications_enabled = models.BooleanField(default=True)

class LanguageChoices(models.TextChoices):
    ENGLISH = 'en', _('English')
    SPANISH = 'es', _('Spanish')
    FRENCH = 'fr', _('French')
    GERMAN = 'de', _('German')
    CHINESE = 'zh', _('Chinese')
    
 class UserPreferenceManager(models.Manager):
    def get_or_create_defaults(self, user):
        return self.get_or_create(user=user, defaults={'theme': 'Light', 'notifications_enabled': True})

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=10, choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Light')
    notifications_enabled = models.BooleanField(default=True)

    objects = UserPreferenceManager()
    
    @receiver(post_save, sender=User)
def create_user_preference(sender, instance, created, **kwargs):
    if created:
        UserPreference.objects.create(user=instance)

def clean(self):
    if self.theme not in dict(ThemeChoices.choices).keys():
        raise ValueError("Invalid theme choice")
