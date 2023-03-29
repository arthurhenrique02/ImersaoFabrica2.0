from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.videogame_store.views import JogoViewSet, LojaViewSet


# criar router para cadastrar rotas da rest api
router = routers.DefaultRouter()
# cadastrar rota de jogos, colocar o JogoViewSet como parametro e definir um nome base
router.register("jogosapi", JogoViewSet, basename="api")
# cadastrar rota de lojas, colocar o LojaViewSet como parametro e definir um nome base
router.register("lojas", LojaViewSet, basename="loja")


urlpatterns = [
    # incluir urls da store
    path("jogos/", include("apps.videogame_store.urls")),

    # incluir router as rotas
    # definir em rota padrao para ser necessario digitar somente "/jogosapi", por exemplo
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
