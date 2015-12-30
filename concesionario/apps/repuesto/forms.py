# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Repuesto
from django.core.urlresolvers import reverse_lazy

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


 