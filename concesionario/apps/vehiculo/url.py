# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import VehiculoCreateView
from .forms import VehiculoUpdateView
from .views import SucursalVehiculosListView
from .views import VehiculosListView
from .forms import AgregarVehiculoSucursalCreateView


urlpatterns = [

    url(r'^vehiculo/crear$', VehiculoCreateView.as_view(), name='crear'),
    url(r'^vehiculo/(?P<pk>\d+)/$', VehiculoUpdateView.as_view(), name='actualizar'), 
    url(r'^vehiculos/$', VehiculosListView.as_view(), name='listar-vehiculos'),
    url(r'^vehiculos/sucursal/(?P<pk>\d+)/$', SucursalVehiculosListView.as_view(), name='listar-vehiculos-sucursal'),
    url(r'^vehiculos/sucursal/agregar', AgregarVehiculoSucursalCreateView.as_view(), name='agregar-vehiculo-sucursal'),

]
