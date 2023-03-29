from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework import viewsets

from .models import Jogo, Loja
from .serializer import JogoSerializer, LojaSerializer


# criar view de jogos
def jogos(request):

    # definir post
    if request.method == "POST":
        return HttpResponse("ola")
    # definir GET por padrao
    jogo = {
        "nome": "CS2",
        "genero": "FPS",
    }

    return JsonResponse(jogo)


# criar viewset para rest api de Jogo
class JogoViewSet(viewsets.ModelViewSet):
    # criar query para consultar todos os dados do jogo
    queryset = Jogo.objects.all()

    # utilizar serializer
    serializer_class = JogoSerializer


# criar viewset para rest api de Loja
class LojaViewSet(viewsets.ModelViewSet):
    # criar query para consultar todos os dados do jogo
    queryset = Loja.objects.all()

    # utilizar serializer
    serializer_class = LojaSerializer
