from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.medicos.models import Medico
from apps.acompanhantes.models import Acompanhante


# criar model
class Paciente(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do funcionario")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200,
        help_text="Sobrenomes do funcionario"
    )

    # idade
    idade = models.IntegerField(
        help_text="Idade do funcionário (apenas numeros)"
    )

    # sexo
    sexo = models.CharField(max_length=1, help_text="Sexo: M ou F")

    # alergias
    alergias = models.CharField(
        max_length=500,
        help_text="Alergias do paciente"
    )

    # tipo sanguineo
    tipo_sangue = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        help_text="Tipo sanguineo do paciente"
    )

    # acompanhante
    # refenciar chave da do acompanhante, permite apenas uma empresa por acompanhante
    acompanhante = models.ForeignKey(
        Acompanhante,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # medico responsavel
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # data e hora de entrada
    data_hora_entrada = models.DateTimeField(
        help_text="Data e hora de entrada"
    )

    # date e hora de saida
    data_hora_saida = models.DateTimeField(
        help_text="Data e hora de saida",
        null=True,
        blank=True
    )

    # retornar o nome e sobrenome
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
