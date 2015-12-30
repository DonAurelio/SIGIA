# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearVehiculo
from .forms import ActualizarVehiculo
from .views import SucursalVehiculosListView
from .views import VehiculosListView
from .views import ParcialVehiculosListView

urlpatterns = [

    url(r'^vehiculo/crear$', CrearVehiculo.as_view(), name='crear'),
    url(r'^vehiculo/(?P<pk>\d+)/$', ActualizarVehiculo.as_view(), name='actualizar'), 
    url(r'^vehiculos/$', VehiculosListView.as_view(), name='listar-vehiculos'),
    url(r'^vehiculos/sucursal/(?P<pk>\d+)/$', SucursalVehiculosListView.as_view(), name='listar-vehiculos-sucursal'),

    url(r'^parcial/vehiculos/', ParcialVehiculosListView.as_view(),name='parcial-listar-vehiculos'),
    
]
