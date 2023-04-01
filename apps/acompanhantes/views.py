from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Acompanhante
from apps.acompanhantes.api.serializer import AcompanhanteSerializer


# criar viewsets
class AcompanhanteViewSet(
    GenericViewSet,  # viewset
    # create (post) read (verifica 1 dado, por exemplo, medico do id 1)
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,  # update (put e patch)
    ListModelMixin  # read (get)
):
    # definir serializer
    serializer_class = AcompanhanteSerializer

    # pegar dados da url
    def get_queryset(self):
        # query set padrao = pegar todos os objetos
        queryset = Acompanhante.objects.all()

        # query para pegar de nome do paciente que está acompanhando
        paciente = self.request.query_params.get("paciente")

        # mudar query de acordo com paciente
        if paciente is not None:
            queryset = Acompanhante.objects.filter(
                paciente_acompanhado=paciente
            )

        # retornar query
        return queryset
