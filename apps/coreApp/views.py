from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# criar rota home
@login_required("login")
def home(request):
    return HttpResponse("ola")
