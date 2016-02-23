# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from apps.sucursal.models import Sucursal, SucursalVehiculo
from .models import Vehiculo
from .forms import VehiculoSucursalCreateForm
from apps.inicio.mixins import LoginRequiredMixin

class VehiculosListView(LoginRequiredMixin, ListView):
	"""Lista todos los vehiculos."""

	model = Vehiculo
	context_object_name = 'vehiculos'
	template_name = 'vehiculo/vehiculo_list.html'

class VehiculoSucursalListView(LoginRequiredMixin, ListView):
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

		sucursal_vehiculos = SucursalVehiculo.objects.filter(sucursal=sucursal)
		return sucursal_vehiculos

	def get_context_data(self,**kwargs):
		"""Perime agregar al contexto la sucursal a la cual pertenecen los vehiculos listados
		en el query_set."""

		context = super(VehiculoSucursalListView,self).get_context_data(**kwargs)
		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['vehiculos'] = Vehiculo.objects.all()


		return context

# Preguntar a Lisa
class VehiculosListSucursal(LoginRequiredMixin, ListView):
 	"""Lista todos los vehiculos con su respectiva sucursal."""

	model = SucursalVehiculo
	context_object_name = 'sucursal_vehiculos'
	template_name = 'vehiculo/inventario_sucursal.html'
