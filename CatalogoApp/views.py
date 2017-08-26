# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CatalogoApp.models import Especie


def index (request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}
    return render(request, 'CatalogoApp/index.html', context)

@csrf_exempt
def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = 'Ok'
        else:
            mensaje = 'Nombre de usuario o clave invalido'

    return JsonResponse({'mensaje':mensaje})

@csrf_exempt
def ingresar(request):
    return render(request, "CatalogoApp/login.html")

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'mensaje':'Ok'})

@csrf_exempt
def isLogged_view(request):
    if request.user.is_authenticated():
        mensaje = 'Ok'
    else:
        mensaje = 'No'

    return JsonResponse({'mensaje':mensaje})
