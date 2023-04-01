from rest_framework import serializers

from apps.medicos.models import Medico


# criar serializer
class MedicoSerializer(serializers.ModelSerializer):
    # criar Meta
    class Meta:
        # definir model
        model = Medico

        # fields à serem serializados
        fields = ("__all__")
