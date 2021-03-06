from django.conf.urls import url

from CatalogoApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^isLogged/$', views.isLogged_view, name="isLogged"),
    url(r'^detalle_especie/(?P<id>.+)/$',views.detalleEspecie, name="detalle_especie"),
    url(r'registro$', views.registro, name='registro'),
    url(r'editar_perfil$', views.editar_perfil, name='editar_perfil'),
    url(r'^Comentario/(?P<id>.+)/$',views.guardarComentario, name="Comentario"),
    url(r'^ingresar/$', views.ingresar, name="ingresar"),
    url(r'^nuevoComentario/(?P<id>.+)/$', views.nuevo_comentario, name="nuevoComentario"),
]
