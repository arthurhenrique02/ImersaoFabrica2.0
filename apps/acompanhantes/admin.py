from django.contrib import admin

from .models import Acompanhante


# criar model para admin
class AcompanhanteAdmin(admin.ModelAdmin):
    model = Acompanhante

    fields = ["nome", "sobrenome", "paciente_acompanhado"]


# registrar model Acompanhante e AcompanhanteAdmin
admin.site.register(Acompanhante, AcompanhanteAdmin)
