# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Proveedor

class ProveedorCreateView(CreateView):
	model = Proveedor
	fields = [
	'nombre','direccion','telefono','ciudad',
	'email','habilitado']
	
	template_name = 'proveedor/proveedor_form.html'
	success_url = reverse_lazy('proveedor:listar')

	def get_context_data(self,**kwargs):
		context = super(ProveedorCreateView,self).get_context_data(**kwargs)
		context['section_name'] = 'Nuevo Proveedor'
		context['button_text'] = 'Crear'
		return context

class ProveedorUpdateView(UpdateView):
	model = Proveedor
	fields = [
	'nombre','direccion','telefono','ciudad',
	'email','habilitado']

	template_name = 'proveedor/proveedor_form.html'
	success_url = reverse_lazy('proveedor:listar')

	def get_context_data(self,**kwargs):
		context = super(ProveedorUpdateView,self).get_context_data(**kwargs)
		context['section_name'] = 'Nuevo Proveedor'
		context['button_text'] = 'Actualizar'
		return context