# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django import forms


class CategoriaEspecie (models.Model):
    nombre = models.CharField(max_length=50)

class TaxonomiaEspecie (models.Model):
    nombre = models.CharField(max_length=50)

class Especie(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_cientifico = models.CharField(max_length=60)
    desc_corta = models.CharField(max_length=150)
    desc_larga = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='images',null=True)
    categoria = models.ForeignKey(CategoriaEspecie, null=False)
    taxonomia = models.ForeignKey(TaxonomiaEspecie, null=False)

class Usuario(models.Model):
    foto = models.ImageField(upload_to='images/user',null=True)
    pais_origen = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    comentario_interes = models.CharField(max_length=1000)
    auth_user_id = models.ForeignKey(User, null = False)

class Comentario(models.Model):
    usuario_id = models.ForeignKey(Usuario, null=False)
    especie_id = models.ForeignKey(Especie, null=False)
    email = models.CharField(max_length=500,null=True)
    fecha = models.DateTimeField(auto_now_add= True, editable=False)
    comentario = models.CharField(max_length=1000, blank=False, null=True)

class UserForm (forms.Form):

    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    foto = forms.ImageField()
    pais_origen = forms.CharField(max_length=60)
    ciudad = forms.CharField(max_length=60)
    comentario_interes = forms.CharField(max_length=1000)
    email = forms.EmailField()
    nombre_usuario = forms.CharField(max_length=50)
    clave = forms.CharField(widget=forms.PasswordInput())
    confirme_clave = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['nombre_usuario']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado')
        return email

    def clean_password2(self):
        password = self.cleaned_data['clave']
        password2 = self.cleaned_data['confirme_clave']

        if password != password2:
            raise forms.ValidationError('Las claves no coinciden')
        return password2