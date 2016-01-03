# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Cotizacion

class ListaCotizaciones(ListView): 
	model = Cotizacion
	context_object_name = 'lista_cotizaciones'