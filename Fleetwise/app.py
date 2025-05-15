from django.apps import AppConfig


class FleetwiseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fleetwise'

    def ready(self):
        """
        Override the ready method to import signals.
        """
        import Fleetwise.signals  # Ensure `Fleetwise/signals.py` exists and is ready for signal definitions
