from django.conf.urls import url

from CatalogoApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ingresar/$', views.ingresar, name="ingresar"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
]