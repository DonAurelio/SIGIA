# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import OrdenDeTrabajo
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo

class OrdenDeTrabajoCreateView(CreateView):
	model = OrdenDeTrabajo
	fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion']
	success_url = reverse_lazy('cuenta:perfil')
	template_name = 'orden_de_trabajo/form.html'

	def get_context_data(self,**kwargs):
		context = super(OrdenDeTrabajoCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Nueva Orden de Trabajo'
		context['vehiculos'] = Vehiculo.objects.all()
		context['clientes'] = Cliente.objects.all()
		return context

	def get_initial(self):
		initial = super(OrdenDeTrabajoCreateView,self).get_initial()
		initial = initial.copy()
		initial['sucursal'] = self.request.user.empleado.sucursal
		initial['empleado'] = self.request.user.empleado
		return initial


class OrdenDeTrabajoUpdateView(UpdateView):
	model = OrdenDeTrabajo
	fields = fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion',
	'fecha_entrada','fecha_salida',
	'habilitado']
	success_url = reverse_lazy('cuenta:perfil')
	template_name = 'orden_de_trabajo/form.html'

	def get_context_data(self,**kwargs):
		context = super(OrdenDeTrabajoUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Orden de Trabajo'
		context['vehiculos'] = Vehiculo.objects.all()
		context['clientes'] = Cliente.objects.all()
		return context

