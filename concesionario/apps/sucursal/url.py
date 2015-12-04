# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearSucursal
from .forms import ActualizarSucursal
from .views import ListaSucursales

urlpatterns = [

    # redirecciona a la pagina de creacion de sucursal
    url(r'^sucursal/crear$', CrearSucursal.as_view(), name='crear-sucursal'),
    # redirecciona a pagina para actualizacion de una sucursal
    url(r'^sucursal/(?P<pk>\d+)/$', ActualizarSucursal.as_view(), name='actualizar-sucursal'), 
    # redirecciona a pagina que despliega el listado de sucursales
    url(r'^sucursal/listado$', ListaSucursales.as_view(), name='lista-sucursales'),
    
]
