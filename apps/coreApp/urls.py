from django.urls import path, include

from .views import home

urlpatterns = [
    # adicionar home ao path
    path('', home, name="home"),

]
