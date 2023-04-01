from django.urls import path, include, re_path

from rest_framework import routers

from .views import AcompanhanteViewSet

# configurar endpoint da api acomapnhante
router = routers.DefaultRouter()
# cadastrar rotas
router.register("", AcompanhanteViewSet, basename="listAcompanhantes")

urlpatterns = [
    # adicionar endpoints da api ao path
    re_path("", include(router.urls)),
]
