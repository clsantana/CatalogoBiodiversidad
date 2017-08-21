# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    categoria = models.ForeignKey(CategoriaEspecie, related_name="ref1")
    taxonomia = models.ForeignKey(TaxonomiaEspecie, related_name="ref1")

