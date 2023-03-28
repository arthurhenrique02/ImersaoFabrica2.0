from django.shortcuts import render
from django.http import HttpResponse


# Criar view para home
def Home(request):
    return HttpResponse("Ola mundo!")
