# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import VehiculoCreateView
from .forms import VehiculoUpdateView
from .views import VehiculosSucursalListView
from .views import VehiculosListView

urlpatterns = [

    url(r'^vehiculo/crear$', VehiculoCreateView.as_view(), name='crear'),
    url(r'^vehiculo/(?P<pk>\d+)/$', VehiculoUpdateView.as_view(), name='actualizar'), 
    url(r'^vehiculos/$', VehiculosListView.as_view(), name='listar-vehiculos'),
    
    # Para el manejo de inventario de vehiculos en una sucursal
    url(r'^vehiculos/sucursal/(?P<pk>\d+)/$', VehiculosSucursalListView.as_view(), name='listar-vehiculos-sucursal'),
    #url(r'^vehiculo/sucursal/inventario/agregar/(?P<pk>)/$',, name='agregar-vehiculo-intentario'),
    
    
]
