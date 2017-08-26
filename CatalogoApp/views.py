# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from CatalogoApp.models import Especie, UserForm, Usuario


def index (request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}
    return render(request, 'CatalogoApp/index.html', context)

def registro (request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('nombre_usuario')
            first_name = data.get('nombre')
            last_name = data.get('apellido')
            password = data.get('clave')
            email = data.get('email')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email

            user_app = Usuario (foto = data.get('foto'),
                                comentario_interes = data.get('comentario_interes'),
                                pais_origen = data.get('pais_origen'),
                                ciudad = data.get('ciudad'),
                                auth_user_id = user_model);
            user_app.save()
            return HttpResponseRedirect(reverse('catalogo:index'))
    else:
        form = UserForm()
        context = {'form' : form}
    return render(request, 'CatalogoApp/registro.html', context)
