# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

import json

from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from sendgrid import sendgrid, Email
from sendgrid.helpers.mail import Content, Mail

from CatalogoApp.models import Especie, UserForm, Usuario, Comentario, CategoriaEspecie, FilterForm, ComentarioForm

def index (request):
    lista_especies = Especie.objects.all()
    if (request.POST):
        filter = FilterForm(request.POST)
        if filter.is_valid():
            data = filter.cleaned_data
            if data.get('listaCategorias') is not None:
                lista_especies = Especie.objects.filter(categoria=data.get('listaCategorias'))
    lista_categorias = FilterForm()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_especies, 4)

    try:
        especies = paginator.page(page)
    except PageNotAnInteger:
        especies = paginator.page(1)
    except EmptyPage:
        especies = paginator.page(paginator.num_pages)

    return render(request, 'CatalogoApp/index.html', {'especies':especies, 'filtro':lista_categorias})

@csrf_exempt
def login_view(request):
    mensaje = ""
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
def logout_view(request):
    logout(request)
    return JsonResponse({'mensaje': 'Ok'})
    #return HttpResponseRedirect(reverse('catalogo:index'))

@csrf_exempt
def isLogged_view(request):
    if request.user.is_authenticated():
        mensaje = 'Ok'
    else:
        mensaje = 'No'

    return JsonResponse({'mensaje':mensaje})

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
            user_model.save()
            user_app.save()
            return HttpResponseRedirect(reverse('catalogo:index'))
    else:
        form = UserForm()
        context = {'form': form}
    return render(request, 'CatalogoApp/registro.html', context)

@login_required
def editar_perfil (request):

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

            user_model = request.user
            user_model.username = username
            #user_model.password = password
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email

            user_app = Usuario.objects.get(auth_user_id=request.user)
            user_app.foto = data.get('foto')
            user_app.comentario_interes = data.get('comentario_interes')
            user_app.pais_origen = data.get('pais_origen')
            user_app.ciudad = data.get('ciudad')

            #user_app = Usuario(foto=data.get('foto'),
            #                   comentario_interes=data.get('comentario_interes'),
            #                   pais_origen=data.get('pais_origen'),
            #                   ciudad=data.get('ciudad'),
            #                   auth_user_id=user_model);

            user_model.save()
            user_app.save()
            return HttpResponseRedirect(reverse('catalogo:index'))
    else:
        usuario = Usuario.objects.get(auth_user_id=request.user)
        print(usuario.foto)
        data = {'nombre': usuario.auth_user_id.first_name,
                 'apellido': usuario.auth_user_id.last_name,
                 'foto': usuario.foto,
                 'pais_origen': usuario.pais_origen,
                 'ciudad': usuario.ciudad,
                 'comentario_interes': usuario.comentario_interes,
                 'email': usuario.auth_user_id.email,
                 'nombre_usuario': usuario.auth_user_id.username,
                 'clave': usuario.auth_user_id.password,
                 'confirme_clave': usuario.auth_user_id.password}
        form = UserForm(data)
        context = {'userForm': form}
    return render(request, 'CatalogoApp/modificar.html', context)

def detalleEspecie(request,id=None):
    especie = Especie.objects.get(id=id)
    lista_comentarios = Comentario.objects.filter(especie_id=id)
    context = {'especie': especie,
               'lista_comentarios':lista_comentarios}
    return render(request, 'CatalogoApp/detalle_especie.html', context)

@csrf_exempt
def guardarComentario(request, id=None):
    especie = Especie.objects.get(id=id)

    #if request.method == 'POST':
    #form = ComentarioForm(request.POST)
    #if form.is_valid():
    #    data = form.cleaned_data

    email = request.POST['email']
    comentario = request.POST['comentario']
    idespecie = especie
    comentario_model = Comentario(especie_id=idespecie, email=email, comentario=comentario)
    comentario_model.save()
    ## Envio de mail
    sg = sendgrid.SendGridAPIClient(apikey="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")
    from_email = Email("coments@grupo4.com")
    to_email = Email(email)
    subject = "Hiciste un comentario!"
    content_full = 'Hola, agradecemos que participes en nuestra página web.\r\n'
    content_full = content_full + 'Recibimos y almacenamos tu comentario: \r\n      \t'
    content_full = content_full + comentario + '\r\n'
    content_full = content_full + 'Favor no responder este correo'
    content = Content("text/plain", content_full)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    #return HttpResponseRedirect(reverse('catalogo:index'))
    #else:
    #    print 'ENTRO AL GET'
    #    form = ComentarioForm()
    #    contexto = {'form': form,
    #                'id':id}
    #    return render(request, 'CatalogoApp/Comentario.html', contexto)
    return JsonResponse({"mensaje": 'OK'})

@csrf_exempt
def ingresar(request):
    return render(request, "CatalogoApp/login.html")

def nuevo_comentario(request,id=None):
    form = ComentarioForm()
    contexto = {'form': form,
               'id':id}
    return render(request,'CatalogoApp/Comentario.html',contexto)
