# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearCotizacion, ActualizarCotizacion
from .views import ListaCotizaciones
from .views import PdfCreateView
urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^cotizacion/crear$', CrearCotizacion.as_view(), name='crear'),	
	url(r'^cotizacion/(?P<pk>\d+)/$', ActualizarCotizacion.as_view(), name='actualizar'),
	url(r'^cotizacion/listado$', ListaCotizaciones.as_view(), name='listar'),
	url(r'^cotizacion/PDF/(?P<pk>\d+)/$', PdfCreateView.as_view(), name='pdf'),
]

  
 
