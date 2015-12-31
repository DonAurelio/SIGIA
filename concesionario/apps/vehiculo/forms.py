# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Vehiculo
from apps.sucursal.models import Sucursal
 
class VehiculoCreateView(CreateView):
	model = Vehiculo
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	success_url = reverse_lazy('vehiculo:listar-vehiculos')

	def get_context_data(self,**kwargs):
		context = super(VehiculoCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Vehiculo'
		context['button_text'] = 'Crear'
		return context


class VehiculoUpdateView(UpdateView):
	model = Vehiculo 
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	success_url = reverse_lazy('vehiculo:listar-vehiculos')

	def get_context_data(self,**kwargs):
		context = super(VehiculoUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Vehiculo'
		context['button_text'] = 'Actualizar'
		return context

"""
class SucursalVehiculoCreateView(CreateView):
	model = SucursalVehiculo
	fields = ['sucursal','vehiculo','color','cantidad','habilitado']
	success_url = reverse_lazy('vehiculo:listar-vehiculos-sucursal')

	#def get_context_data(**kwargs):
	#	context = super(SucursalVehiculoCreateView,self).get_context_data(**kwargs)
	#	sucursal = Sucursal.objects.get(id=kwargs['pk'])
		

	#	return context
"""