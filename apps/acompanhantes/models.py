from django.db import models


# Criar model
class Acompanhante(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do acompanhante")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenome do acompanhante")

    # retornar o nome e sobrenome
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
