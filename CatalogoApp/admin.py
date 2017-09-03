# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CategoriaEspecie, Especie, TaxonomiaEspecie,Usuario,Comentario

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre', )

class TaxonomiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )

class EspeciesAdmin(admin.ModelAdmin):
    list_display = ('nombre','nombre_cientifico','desc_corta','desc_larga','foto','get_categoria','get_taxonomia' )

    def get_categoria(self, obj):
        return obj.categoria.nombre

    get_categoria.short_description = 'Categoria'
    get_categoria.admin_order_field = 'nombre'

    def get_taxonomia(self, obj):
        return obj.taxonomia.nombre

    get_taxonomia.short_description = 'Taxonomía'
    get_taxonomia.admin_order_field = 'nombre'

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('foto','pais_origen','ciudad','comentario_interes')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('especie_id','email','fecha','comentario')

# Register your models here.
admin.site.register(CategoriaEspecie, CategoriasAdmin)
admin.site.register(TaxonomiaEspecie, TaxonomiaAdmin)
admin.site.register(Especie, EspeciesAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Comentario, ComentarioAdmin)