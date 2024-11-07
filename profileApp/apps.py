from django.apps import AppConfig


class ProfileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profileApp'

    def ready(self):
        import profileApp.signals  # Import signals to make them work