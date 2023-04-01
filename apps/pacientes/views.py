from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Paciente
from apps.pacientes.api.serializer import PacienteSerializer


# criar viewsets
class PacienteViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin
):
    # definir serializer
    serializer_class = PacienteSerializer

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
