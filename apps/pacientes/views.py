from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination

from .models import Paciente
from apps.pacientes.api.serializer import PacienteSerializer


# criar viewsets
class PacienteViewSet(
    GenericViewSet,  # viewset
    CreateModelMixin,  # create (post)
    RetrieveModelMixin,  # read (verifica 1 dado, por exemplo, medico do id 1)
    UpdateModelMixin,  # update (put e patch)
    ListModelMixin,  # read (get)
    DestroyModelMixin  # delete
):
    # definir serializer
    serializer_class = PacienteSerializer

    # definir paginação
    pagination_class = LimitOffsetPagination  # adicionar ?limit=(num) a url

    # pegar dados da url
    def get_queryset(self):
        # query set padrao (pegar todos os dados)
        queryset = Paciente.objects.all()

        # solicitar query de acordo com o medico q está acompanhando
        medico = self.request.query_params.get("medico")

        if medico is not None:
            queryset = Paciente.objects.filter(medico=medico)

        # retornar query
        return queryset
