from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'library'

from django.apps import AppConfig

class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    def ready(self):
        import library.signals
