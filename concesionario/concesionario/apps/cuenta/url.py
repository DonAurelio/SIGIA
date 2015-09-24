from django.conf.urls import include, url
from django.contrib import admin
from .views import PerfilGerente
from .views import PerfilJefeTaller
from .views import PerfilVendedor

urlpatterns = [
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include( admin.site.urls ) name="admin"),
    url(r'^cuenta/gerente/$', PerfilGerente.as_view(), name="gerente"),
    url(r'^cuenta/jefe_taller/$', PerfilJefeTaller.as_view(), name="jefe_taller"),
    url(r'^cuenta/vendedor/$', PerfilVendedor.as_view(), name="vendedor"),
]
