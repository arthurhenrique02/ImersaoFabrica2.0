from django.contrib import admin

from .models import Paciente


# criar model para admin
class PacienteAdmin(admin.ModelAdmin):
    model = Paciente

    fields = [
        "nome", "sobrenome", "idade", "sexo",
        "alergias", "tipo_sangue", "medico"
    ]


# registrar model Acompanhante e AcompanhanteAdmin
admin.site.register(Paciente, PacienteAdmin)
