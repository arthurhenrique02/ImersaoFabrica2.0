from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # incluir urls da store
    path("jogos/", include("apps.videogame_store.urls")),

    path('admin/', admin.site.urls),
]
