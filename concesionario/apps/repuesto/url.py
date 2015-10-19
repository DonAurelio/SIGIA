# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearRepuesto
from .views import ListaRepuestos
from .views import DetallesRepuesto

urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^repuesto/crear$', CrearRepuesto.as_view(), name='crear'),
    #url que redirecciona a pagina que despliega el listado de repuestos
	url(r'^repuesto/listado$', ListaRepuestos.as_view(), name='lista-repuestos'),
	#url que redirecciona a la pagina de detalles de un repuesto
	url(r'^repuesto/detalles/(?P<pk>[0-9]+)/$', DetallesRepuesto.as_view(), name='detalles-repuesto'),
]
