from django.contrib import admin

from .models import Jogo, Loja, Cliente


# criar display para jogo no admin
class JogoAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero", "ano", "preco")


# criar displayr para loja no admin
class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "endereco", "telefone")

# criar displayr para cliente no admin


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "endereco", "telefone")


# registrar Jogo, Loja e Cliente
admin.site.register(Jogo, JogoAdmin)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Cliente, ClienteAdmin)
