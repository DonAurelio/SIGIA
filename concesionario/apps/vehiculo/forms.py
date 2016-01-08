# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Vehiculo
from apps.sucursal.models import Sucursal
from apps.sucursal.models import SucursalVehiculo
from django import forms
 
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

class VehiculoSucursalCreateForm(forms.ModelForm):
	class Meta:
		model = SucursalVehiculo
		fields = ('vehiculo','sucursal','color','cantidad','habilitado')

class VehiculoSucursalCreateView(CreateView):
	model = SucursalVehiculo
	template_name  = 'vehiculo/inventario_list.html'
	fields = ['vehiculo','sucursal','color','cantidad','habilitado']
	
	def get_context_data(self,**kwargs):
		context = super(VehiculoSucursalCreateView,self).get_context_data(**kwargs)
		# Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
		#context['vehiculos']  = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
		context['vehiculos'] =  Vehiculo.objects.all()
		context['form_mode'] = 'create'
		context['sucursal'] = Sucursal.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('vehiculo:listar-vehiculos-sucursal',kwargs={'pk':self.kwargs['pk']})


class VehiculoSucursalUpdateView(UpdateView):
	model = SucursalVehiculo
	template_name  = 'vehiculo/inventario_list.html'
	fields = ['vehiculo','sucursal','color','cantidad','habilitado']
	
	def get_context_data(self,**kwargs):
		context = super(VehiculoSucursalUpdateView,self).get_context_data(**kwargs)
		# Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
		#context['vehiculos']  = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
		context['vehiculos'] =  Vehiculo.objects.all()
		context['form_mode'] = 'update'
		sucursal_vehiculo = SucursalVehiculo.objects.get(id=self.kwargs['pk'])
		sucursal_id = sucursal_vehiculo.sucursal_id
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		#context['sucursal_vehiculo'] = sucursal_vehiculo
		context['sucursal_vehiculos'] = SucursalVehiculo.objects.filter(sucursal=sucursal)

		return context

	def get_success_url(self):
		sucursal_vehiculo = SucursalVehiculo.objects.get(id=self.kwargs['pk'])
		return reverse_lazy('vehiculo:listar-vehiculos-sucursal',kwargs={'pk':sucursal_vehiculo.sucursal.id})
