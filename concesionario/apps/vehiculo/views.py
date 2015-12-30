# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Vehiculo, SucursalVehiculo
from apps.sucursal.models import Sucursal

class VehiculosListView(ListView):
	"""Lista todos los vehiculos."""

	model = Vehiculo
	context_object_name = 'vehiculos'
	template_name = 'vehiculo/vehiculo_list.html'

class SucursalVehiculosListView(ListView): 
	"""Lista los vehiculos por sucursal."""
	
	model = SucursalVehiculo
	context_object_name = 'sucursal_vehiculos'
	template_name = 'vehiculo/inventario_list.html'

	def get_queryset(self):
		'''Permite filtrar los vehiculos que seran mostrados.

		Dada la pk de la sucursal se sobre escribe el metodo
		para que se listen los vehiculos que pertenecen a una
		sucursal dada.

		'''

		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		vehiculos = sucursal.vehiculo_set.all()

		sucursal_vehiculos = SucursalVehiculo.objects.filter(sucursal=sucursal)
		return sucursal_vehiculos

	def get_context_data(self,**kwargs):
		"""Perime agregar al contexto la sucursal a la cual pertenecen los vehiculos listados
		en el query_set."""

		context = super(SucursalVehiculosListView,self).get_context_data(**kwargs)
		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		return context

class ParcialVehiculosListView(ListView):
	"""Lista todos los vehiculos."""

	model = Vehiculo
	context_object_name = 'vehiculos'
	template_name = 'vehiculo/parcial/vehiculo_list.html'