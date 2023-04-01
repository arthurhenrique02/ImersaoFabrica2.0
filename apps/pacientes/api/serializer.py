from rest_framework import serializers

from apps.pacientes.models import Paciente


# criar serializer
class PacienteSerializer(serializers.ModelSerializer):
    # criar Meta
    class Meta:
        # definir model
        model = Paciente

        # fields à serem serializados
        fields = [
            "nome", "sobrenome", "idade", "sexo", "alergias",
            "tipo_sangue", "acompanhante", "data_hora_entrada",
            "data_hora_saida"
        ]
