# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    foto = models.ImageField(upload_to='images',null=True)
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

