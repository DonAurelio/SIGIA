# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearVenta
from .forms import ActualizarVenta
from .views import ListaVentas

urlpatterns = [

    # redirecciona a la pagina de creacion de venta
    url(r'^venta/crear$', CrearVenta.as_view(), name='crear'),
    # redirecciona a pagina para actualizacion de una venta
    url(r'^venta/(?P<pk>\d+)/$', ActualizarVenta.as_view(), name='actualizar'),
    # redirecciona a pagina que despliega el listado de ventas
    url(r'^venta/listado$', ListaVentas.as_view(), name='listar'),
    
]
