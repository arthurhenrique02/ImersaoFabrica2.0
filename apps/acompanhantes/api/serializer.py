from rest_framework import serializers

from apps.acompanhantes.models import Acompanhante


# criar serializer
class AcompanhanteSerializer(serializers.ModelSerializer):
    # criar Meta
    class Meta:
        # definir model
        model = Acompanhante

        # fields à serem serializados
        fields = [
            "nome", "sobrenome",

        ]
