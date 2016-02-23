# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Proveedor
from apps.inicio.mixins import LoginRequiredMixin

class ProveedorCreateView(LoginRequiredMixin, CreateView):
	model = Proveedor
	fields = [
	'nombre','direccion','telefono','ciudad',
	'email','habilitado']

	template_name = 'proveedor/form.html'
	success_url = reverse_lazy('proveedor:listar')

	def get_context_data(self,**kwargs):
		context = super(ProveedorCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Proveedor'
		return context


class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
	model = Proveedor
	fields = [
	'nombre','direccion','telefono','ciudad',
	'email','habilitado']

	template_name = 'proveedor/form.html'
	success_url = reverse_lazy('proveedor:listar')

	def get_context_data(self,**kwargs):
		context = super(ProveedorUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Proveedor'
		return context
