# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearVenta
from .forms import ActualizarVenta
from .views import ListaVentas
from .views import FacturaCreateView


urlpatterns = [ 

    # redirecciona a la pagina de creacion de venta
    url(r'^venta/crear$', CrearVenta.as_view(), name='crear'),
    # redirecciona a pagina que despliega el listado de ventas
    url(r'^venta/listado$', ListaVentas.as_view(), name='listar'),
 	#factura 
 	url(r'^venta/factura/(?P<pk>\d+)/$', FacturaCreateView.as_view(), name='factura'),
    
]
