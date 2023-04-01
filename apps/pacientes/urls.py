from django.urls import path, include

from rest_framework import routers

from .views import PacienteViewSet

# configurar endpoint da api paciente
router = routers.DefaultRouter()
# cadastrar rotas
router.register(r"^(?P<q>\d+)/", PacienteViewSet, basename="listPacientes")

urlpatterns = [
    # adicionar endpoints da api ao path
    path("", include(router.urls)),
]
