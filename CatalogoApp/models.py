# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CategoriaEspecie (models.Model):
    nombre = models.CharField(max_length=50)