from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Medico
from apps.medicos.api.serializer import MedicoSerializer


# criar viewsets
class MedicoViewSet(
    GenericViewSet,  # viewset
    # create (post) read (verifica 1 dado, por exemplo, medico do id 1)
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,  # update (put e patch)
    ListModelMixin  # read (get)
):
    # definir serializer
    serializer_class = MedicoSerializer

    # pegar dados da url
    def get_queryset(self):
        # query set padrao = pegar todos os objetos
        queryset = Medico.objects.all()

        # query para pegar medico por area de atuação
        area_atuacao = self.request.query_params.get("area_atuacao")

        # mudar query para medicos da área desejada
        if area_atuacao is not None:
            queryset = Medico.objects.filter(area_atuacao=area_atuacao)

        # retornar query
        return queryset
