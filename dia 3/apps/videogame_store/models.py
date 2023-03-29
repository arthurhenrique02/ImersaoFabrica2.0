from django.db import models


# criar model para jogo
class Jogo(models.Model):
    # nome do jogo
    nome = models.CharField(max_length=100, help_text="Nome do jogo")

    # genero
    genero = models.CharField(
        max_length=100,
        help_text="Genero do jogo. Ex: ação"
    )

    # ano de lançamento do jogo
    ano = models.CharField(max_length=4, help_text="Ano de lançamento")

    # preço do jogo
    # max digits para quantidade maxima e decimal places para quantidade maxima de numeros após o float
    preco = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="preço do jogo")

    # retornar nome do jogo
    def __str__(self):
        return self.nome


# model para loja
class Loja(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da loja")

    # endereço
    endereco = models.CharField(max_length=100, help_text="Endereço da loja")

    # numero de telefone
    telefone = models.CharField(
        max_length=20, help_text="Telefone para contato da loja")

    # retornar nome da loja
    def __str__(self):
        return self.nome
