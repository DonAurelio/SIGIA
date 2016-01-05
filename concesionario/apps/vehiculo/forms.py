# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Vehiculo
from apps.sucursal.models import SucursalVehiculo
 
class CrearVehiculo(CreateView):
	model = Vehiculo
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	success_url = reverse_lazy('vehiculo:listar-vehiculos')

	def get_context_data(self,**kwargs):
		context = super(CrearVehiculo,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Vehiculo'
		context['button_text'] = 'Crear'
		return context


class ActualizarVehiculo(UpdateView):
	model = Vehiculo 
	fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
	'capacidad', 'caracteristicas', 'imagen', 'precio']
	success_url = reverse_lazy('vehiculo:listar-vehiculos')

	def get_context_data(self,**kwargs):
		context = super(ActualizarVehiculo,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Vehiculo'
		context['button_text'] = 'Actualizar'
		return context


class AgregarVehiculoSucursalCreateView(CreateView):
	model = SucursalVehiculo
	fields = ['vehiculo','sucursal','color','cantidad']
	success_url = reverse_lazy('vehiculo:agregar-vehiculo-sucursal')

	def get_context_data(self,**kwargs):
		context = super(AgregarVehiculoSucursalCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Agregar Vehiculo al Inventario'
		context['button_text'] = 'Agregar'
		context['veiculos'] = Vehiculo.objects.all()
		return context
