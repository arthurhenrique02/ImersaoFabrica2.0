from django.apps import AppConfig


class CoreappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # alterar no da app para apps.coreApp
    name = 'apps.coreApp'
