from django.urls import path, include, re_path

from rest_framework import routers

from .views import PacienteViewSet

# configurar endpoint da api paciente
router = routers.DefaultRouter()
# cadastrar rotas
router.register("",
                PacienteViewSet, basename="listPacientes")

urlpatterns = [
    # adicionar endpoints da api ao path
    re_path("", include(router.urls)),
]
