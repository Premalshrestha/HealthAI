from django.apps import AppConfig


class MediappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mediapp'

    def ready(self):
        import mediapp.signals  # replace with your actual app name