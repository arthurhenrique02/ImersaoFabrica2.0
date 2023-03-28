from django.urls import path, include

# importar view
from .views import Home

urlpatterns = [
    # setar como root e definir nome da URL (home)
    path("", Home, name="home"),
]
