# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearRepuesto
from .forms import ActualizarRepuesto
from .views import RepuestosSucursalListView
from .views import RepuestosListView

urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^repuesto/crear$', CrearRepuesto.as_view(), name='crear'),
    #url que redirecciona a pagina que despliega el listado de repuestos por sucursal
    url(r'^repuesto/sucursal/(?P<pk>\d+)/$', RepuestosSucursalListView.as_view(), name='listar-repuestos-sucursal'),
    #redirecciona a pagina para actualizacion de un repuesto
    url(r'^repuesto/(?P<pk>\d+)/$', ActualizarRepuesto.as_view(), name='actualizar'), 

    url(r'^repuestos/$', RepuestosListView.as_view(), name='listar'), 
    
]
