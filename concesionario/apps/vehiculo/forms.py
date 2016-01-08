# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Vehiculo
from apps.sucursal.models import Sucursal
from apps.sucursal.models import SucursalVehiculo
 
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

class VehiculoSucursalCreateView(CreateView):
	model = SucursalVehiculo
	template_name  = 'vehiculo/inventario_form.html'
	fields = ['vehiculo','sucursal','color','cantidad','habilitado']
	
	def get_context_data(self,**kwargs):
		context = super(VehiculoSucursalCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Vehículos Disponibles'
		context['submit_button_text'] = 'Agregar'
		context['search_button_text'] = 'Seleccionar vehiculo'
		
		# Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
		#vehiculos = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
		vehiculos = Vehiculo.objects.all()
		context['vehiculos'] = vehiculos
		
		return context

	def get_initial(self):
		initial = super(VehiculoSucursalCreateView,self).get_initial()
		initial = initial.copy()
		initial['sucursal'] = Sucursal.objects.get(id=self.kwargs['pk'])
		return initial

	def get_success_url(self):
		return reverse_lazy('vehiculo:listar-vehiculos-sucursal',kwargs={'pk':self.kwargs['pk']})
