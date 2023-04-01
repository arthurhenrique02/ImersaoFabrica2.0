from django.db import models


# criar model
class Medico(models.Model):
    # nome
    nome = models.CharField(max_length=30, help_text="Nome do medico")

    # sobrenome
    sobrenome = models.CharField(
        max_length=200, help_text="Sobrenome do medico")

    # crm
    crm = models.CharField(max_length=20, help_text="CRM do médico")

    # area de atuação
    area_atuacao = models.CharField(max_length=60, help_text="Área de atuação")

    # retornar o nome e sobrenome
    def __str__(self):
        return self.nome
