# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from .models import Vehiculo
 
class CrearVehiculo(CreateView):
	model = Vehiculo
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio', 'habilitado']

	def get_context_data(self,**kwargs):
		context = super(CrearVehiculo,self).get_context_data(**kwargs)
		context['section_title'] = "Nuevo Vehiculo"
		context['button_text'] = 'Crear'

		return context


class ActualizarVehiculo(UpdateView):
	model = Vehiculo 
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio', 'sucursal']