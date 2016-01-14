# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import OrdenDeTrabajo

class OrdenDeTrabajoCreateView(CreateView):
	model = OrdenDeTrabajo
	fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion']
	success_url = reverse_lazy('cuenta:perfil')

	def get_context_data(self,**kwargs):
		context = super(OrdenDeTrabajoCreateView,self).get_context_data(**kwargs)
		context['section_name'] = 'Nueva Orden de Trabajo'
		return context

class OrdenDeTrabajoUpdateView(UpdateView):
	model = OrdenDeTrabajo
	fields = fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion',
	'fecha_entrada','fecha_salida',
	'habilitado']
	success_url = reverse_lazy('cuenta:perfil')

	def get_context_data(self,**kwargs):
		context = super(OrdenDeTrabajoUpdateView,self).get_context_data(**kwargs)
		context['section_name'] = 'Actualizar Orden de Trabajo'
		return context

