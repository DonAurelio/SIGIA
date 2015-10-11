from django.conf.urls import include, url
from .forms import CrearCotizacion

urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^cotizacion/crear$', CrearCotizacion.as_view(), name='crear'),
]
