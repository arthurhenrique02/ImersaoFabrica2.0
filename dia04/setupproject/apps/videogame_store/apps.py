from django.apps import AppConfig


class VideogameStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # renomear nome, colocar o path "apps." no inicio
    name = 'apps.videogame_store'
