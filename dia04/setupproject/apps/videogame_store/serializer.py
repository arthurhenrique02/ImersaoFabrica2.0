from rest_framework import serializers

from .models import Jogo, Loja, Cliente


# criar serializer para Jogo
class JogoSerializer(serializers.ModelSerializer):
    # criar classe Meta
    class Meta:
        # selecionar model Jogo
        model = Jogo

        # definir fields à serem serialiados
        fields = ["nome", "genero", "ano", "preco"]


# criar serializer para Loja
class LojaSerializer(serializers.ModelSerializer):
    # criar classe Meta
    class Meta:
        # selecionar model Loja
        model = Loja

        # definir fields
        fields = ["nome", "endereco", "telefone"]


# criar serializer para cliente
class ClienteSerializer(serializers.ModelSerializer):
    # criar classe Meta
    class Meta:
        # selecionar model Loja
        model = Loja

        # definir fields
        fields = ["nome", "endereco", "telefone"]
