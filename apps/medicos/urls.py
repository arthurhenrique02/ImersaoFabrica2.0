from django.urls import path, include, re_path

from rest_framework import routers

from .views import MedicoViewSet

# configurar endpoint da api medico
router = routers.DefaultRouter()
# cadastrar rotas
router.register("", MedicoViewSet, basename="listMedicos")

urlpatterns = [
    # adicionar endpoints da api ao path
    re_path("", include(router.urls)),
]
