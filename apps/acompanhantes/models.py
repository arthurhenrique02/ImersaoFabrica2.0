from django.db import models

from apps.pacientes.models import Paciente


# Criar model
class Acompanhante(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do acompanhante")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenome do acompanhante")

    # paciente
    paciente_acompanhado = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
    )

    # retornar o nome e sobrenome
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
