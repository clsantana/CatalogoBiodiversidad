# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CategoriaEspecie, Especie, TaxonomiaEspecie

# Register your models here.
admin.site.register(CategoriaEspecie)
admin.site.register(TaxonomiaEspecie)
admin.site.register(Especie)

