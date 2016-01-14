# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Repuesto
from apps.sucursal.models import Sucursal, SucursalRepuesto
from django.core.urlresolvers import reverse_lazy
from django import forms

class CrearRepuesto(CreateView): 
	model = Repuesto
	fields = ['nombre', 'precio', 'marca', 'clasificacion',
	'imagen', 'proveedor', 'descripcion']
	success_url = reverse_lazy('repuesto:listar')

	def get_context_data(self,**kwargs):
		context = super(CreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Repuesto'
		context['button_text'] = 'Crear'
		return context

class ActualizarRepuesto(UpdateView): 
	model = Repuesto 
	fields = ['nombre', 'precio', 'marca', 'clasificacion',
	'imagen', 'proveedor', 'descripcion']
	success_url = reverse_lazy('repuesto:listar')

	def get_context_data(self,**kwargs):
		context = super(ActualizarRepuesto,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Repuesto'
		context['button_text'] = 'Actualizar'
		return context

class RepuestoSucursalCreateForm(forms.ModelForm):
	class Meta:
		model = SucursalRepuesto
		fields = ('sucursal','repuesto','cantidad','habilitado')

class RepuestoSucursalCreateView(CreateView):
	model = SucursalRepuesto
	template_name  = 'repuesto/inventario_list.html'
	fields = ['sucursal','repuesto','cantidad','habilitado']
	
	def get_context_data(self,**kwargs):
		context = super(RepuestoSucursalCreateView,self).get_context_data(**kwargs)
		context['repuestos'] =  Repuesto.objects.all()
		context['form_mode'] = 'create'
		context['sucursal'] = Sucursal.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('repuesto:listar-repuestos-sucursal',kwargs={'pk':self.kwargs['pk']})


class RepuestoSucursalUpdateView(UpdateView):
	model = SucursalRepuesto
	template_name  = 'repuesto/inventario_list.html'
	fields = ['sucursal','repuesto','cantidad','habilitado']
	
	def get_context_data(self,**kwargs):
		context = super(RepuestoSucursalUpdateView,self).get_context_data(**kwargs)
		# Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
		#context['vehiculos']  = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
		context['repuestos'] =  Repuesto.objects.all()
		context['form_mode'] = 'update'
		sucursal_repuesto = SucursalRepuesto.objects.get(id=self.kwargs['pk'])
		sucursal_id = sucursal_repuesto.sucursal_id
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['sucursal_repuestos'] = SucursalRepuesto.objects.filter(sucursal=sucursal)

		return context

	def get_success_url(self):
		sucursal_repuesto = SucursalRepuesto.objects.get(id=self.kwargs['pk'])
		return reverse_lazy('repuesto:listar-repuestos-sucursal',kwargs={'pk':sucursal_repuesto.sucursal.id})
