from django.conf.urls import include, url
from django.contrib import admin
from .views import Inicio, IniciarSesion, PerfilGerente, PerfilJefeTaller, PerfilVendedor


urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Inicio.as_view(), name="inicio"),
    url(r'^iniciar_sesion/$', IniciarSesion.as_view(), name="iniciar_sesion"),
    url(r'^perfil_gerente/$', PerfilGerente.as_view(), name="perfil_gerente"),
    url(r'^perfil_jefe_taller/$', PerfilJefeTaller.as_view(), name="perfil_jefe_taller"),
    url(r'^perfil_vendedor/$', PerfilVendedor.as_view(), name="perfil_vendedor"),
    
    
]
