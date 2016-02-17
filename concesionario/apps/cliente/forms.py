# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Cliente

# Crea el registro de un cliente mediante la clase generica CreateView
class CrearCliente(CreateView):
	model = Cliente
	fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
	'departamento', 'telefono', 'celular', 'email']
	success_url = reverse_lazy('cliente:listar')
	template_name = "cliente/form.html"

	def get_context_data(self,**kwargs):
		context = super(CrearCliente,self).get_context_data(**kwargs)
		context['section_title'] = 'Nuevo Cliente'
		return context


class ActualizarCliente(UpdateView):
	model = Cliente
	fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
	'departamento', 'telefono', 'celular', 'email']
	success_url = reverse_lazy('cliente:listar')
	template_name = "cliente/form.html"

	def get_context_data(self,**kwargs):
		context = super(ActualizarCliente,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Cliente'
		return context
