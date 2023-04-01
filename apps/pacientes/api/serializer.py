from rest_framework import serializers

from apps.pacientes.models import Paciente


# criar serializer
class PacienteSerializer(serializers.ModelSerializer):
    # criar Meta
    class Meta:
        # definir model
        model = Paciente

        # fields à serem serializados
        fields = ("__all__")
