# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import VehiculoCreateView
from .forms import VehiculoUpdateView
from .views import VehiculosListView

from .forms import VehiculoSucursalAjaxCreateView
from .forms import VehiculoSucursalAjaxUpdateView
from .views import VehiculoSucursalListView

from .views import VehiculosListSucursal

urlpatterns = [

    url(r'^vehiculo/crear$', VehiculoCreateView.as_view(), name='crear'),
    url(r'^vehiculo/(?P<pk>\d+)/$', VehiculoUpdateView.as_view(), name='actualizar'), 
    url(r'^vehiculos/$', VehiculosListView.as_view(), name='listar-vehiculos'),
    
    url(r'^vehiculos/sucursal/(?P<spk>\d+)/agregar/(?P<vpk>\d+)/$', VehiculoSucursalAjaxCreateView.as_view(), name='agregar-vehiculo-sucursal'),
    url(r'^vehiculos/sucursal/actualizar/(?P<pk>\d+)/$', VehiculoSucursalAjaxUpdateView.as_view(), name='actualizar-vehiculo-sucursal'),
    url(r'^vehiculos/sucursal/(?P<pk>\d+)/$', VehiculoSucursalListView.as_view(), name='listar-vehiculos-sucursal'),
        
    url(r'^vehiculos/inventario$', VehiculosListSucursal.as_view(), name='listar-vehiculos-inventario'),
]
