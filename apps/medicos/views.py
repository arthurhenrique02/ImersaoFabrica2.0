from django.shortcuts import render
from rest_framework import viewsets

from .models import Medico
from apps.medicos.api.serializer import MedicoSerializer


# criar viewsets
class MedicoViewSet(viewsets.ModelViewSet):
    # adicionar model
    # solicitar todos os dados, por enquanto
    queryset = Medico.objects.all()

    # utilizar serializer
    serializer_class = MedicoSerializer
