# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearRepuesto
from .forms import ActualizarRepuesto
from .views import ListaRepuestos

urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^repuesto/crear$', CrearRepuesto.as_view(), name='crear'),
    #url que redirecciona a pagina que despliega el listado de repuestos
    url(r'^repuesto/listado$', ListaRepuestos.as_view(), name='lista-repuestos'),
    #redirecciona a pagina para actualizacion de un repuesto
    url(r'^repuesto/(?P<pk>\d+)/$', ActualizarRepuesto.as_view(), name='actualizar-repuesto'), 
    
]
