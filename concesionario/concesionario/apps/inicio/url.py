from django.conf.urls import include, url
from django.contrib import admin
from .views import IniciarSesion
from .views import CerrarSesion


urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IniciarSesion.as_view(), name="inicio"),
    url(r'^cerrar_sesion/$', CerrarSesion.as_view(), name="cerrar_sesion"),
]
