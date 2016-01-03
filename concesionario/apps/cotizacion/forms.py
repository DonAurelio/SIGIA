# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Cotizacion 
 
  
class CrearCotizacion(CreateView): 

	model = Cotizacion 
	fields = ['empleado', 'cliente', 'vehiculo', 'fecha','fecha_vencimiento', 'forma_pago'] 
	success_url = reverse_lazy('cotizacion:listar') 


class ActualizarCotizacion(UpdateView): 
    model = Cotizacion 
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha','fecha_vencimiento', 'forma_pago'] 
    success_url = reverse_lazy('cotizacion:listar') 
