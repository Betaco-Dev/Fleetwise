from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fleetwise'

    def ready(self):
        import Fleetwise.signals  # Replace `your_app_name` with your actual app name
