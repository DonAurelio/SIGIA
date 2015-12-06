# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearVehiculo
from .forms import ActualizarVehiculo
from .views import ListaVehiculos

urlpatterns = [

    # redirecciona a la pagina de creacion de vehiculo
    url(r'^vehiculo/crear$', CrearVehiculo.as_view(), name='crear'),
    # redirecciona a pagina para actualizacion de un vehiculo
    url(r'^vehiculo/(?P<pk>\d+)/$', ActualizarVehiculo.as_view(), name='actualizar'), 
    # redirecciona a pagina que despliega el listado de vehiculos
    url(r'^vehiculo/listado$', ListaVehiculos.as_view(), name='listar'),
    
]
