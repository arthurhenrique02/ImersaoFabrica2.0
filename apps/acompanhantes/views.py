from django.shortcuts import render
from rest_framework import viewsets

from .models import Acompanhante
from apps.acompanhantes.api.serializer import AcompanhanteSerializer


# criar viewsets
class AcompanhanteViewSet(viewsets.ModelViewSet):
    # adicionar model
    # solicitar todos os dados, por enquanto
    queryset = Acompanhante.objects.all()

    # utilizar serializer
    serializer_class = AcompanhanteSerializer
