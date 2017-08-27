from django.conf.urls import url

from CatalogoApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'registro$', views.registro, name='registro'),
    url(r'editar_perfil$', views.editar_perfil, name='editar_perfil'),
]