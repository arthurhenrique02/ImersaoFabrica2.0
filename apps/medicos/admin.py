from django.contrib import admin

from .models import Medico


# criar model para admin
class MedicoAdmin(admin.ModelAdmin):
    model = Medico

    fields = ["nome", "sobrenome", "crm", "area_atuacao",]


# registrar model Acompanhante e AcompanhanteAdmin
admin.site.register(Medico, MedicoAdmin)
