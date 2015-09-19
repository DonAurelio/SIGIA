from django.conf.urls import include, url
from django.contrib import admin
from .views import PerfilGerente
from .views import PerfilJefeTaller
from .views import PerfilVendedor

urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cuenta/perfil_gerente/$', PerfilGerente.as_view(), name="perfil_gerente"),
    url(r'^cuenta/perfil_jefe_taller/$', PerfilJefeTaller.as_view(), name="perfil_jefe_taller"),
    url(r'^cuenta/perfil_vendedor/$', PerfilVendedor.as_view(), name="perfil_vendedor"),
]
