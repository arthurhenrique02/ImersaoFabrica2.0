from django.shortcuts import render
from rest_framework import viewsets

from .models import Paciente
from apps.pacientes.api.serializer import PacienteSerializer


# criar viewsets
class PacienteViewSet(viewsets.ModelViewSet):
    # adicionar model
    # solicitar todos os dados, por enquanto
    queryset = Paciente.objects.all()

    # utilizar serializer
    serializer_class = PacienteSerializer
