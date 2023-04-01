from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.medicos.models import Medico
from apps.pacientes.models import Paciente
from apps.acompanhantes.models import Acompanhante

# criar rota home


@login_required(login_url="accounts/login")
def home(request):
    return render(request, "index.html")
