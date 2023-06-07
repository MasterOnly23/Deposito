from django.apps import AppConfig


class RacksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Racks'

    def ready(self):
        import Racks.signals