from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # adicionar accounts url (padrao do django)
    path('accounts/', include('django.contrib.auth.urls')),
    # adicionar rotar dos medicos ao path
    path("medicos/", include("apps.medicos.urls"), name="medicos"),
    # adicionar rotar dos acompanhantes ao path
    path("acompanhantes/", include("apps.acompanhantes.urls"), name="acompanhantes"),
    # adicionar rotar dos pacientes ao path
    path("pacientes/", include("apps.pacientes.urls"), name="pacientes"),

    path("", include("apps.coreApp.urls")),
]
