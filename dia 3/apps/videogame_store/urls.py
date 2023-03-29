from django.contrib import admin
from django.urls import path

from .views import jogos

urlpatterns = [
    path('', jogos),
]
