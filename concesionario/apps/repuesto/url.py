# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from apps.repuesto.forms import CrearRepuesto

urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^repuesto/crear$', CrearRepuesto.as_view(), name='crear'),
]
