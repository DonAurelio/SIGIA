# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .models import OrdenDeTrabajo
from .models import RETIRADO
from .models import REPARADO_Y_ENTREGADO
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo
from apps.inicio.mixins import LoginRequiredMixin

class OrdenDeTrabajoCreateView(LoginRequiredMixin, CreateView):
	model = OrdenDeTrabajo
	fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion']
	success_url = reverse_lazy('orden_de_trabajo:listar')
	template_name = 'orden_de_trabajo/form.html'

	def post(self,request,*args,**kwargs):
		form = self.get_form(self.get_form_class())
		if form.is_valid():
			placa = form.cleaned_data['placa']
			ordenes_de_trabajo = OrdenDeTrabajo.objects.filter(placa=placa,fecha_salida=None)
			if ordenes_de_trabajo:
				messages.info(request,"El vehiculo con placa {} ya tiene una orden de trabajo".format(placa))
				return self.get(request,args,kwargs)
			else:
				return super(OrdenDeTrabajoCreateView,self).post(request,args,kwargs)
		else:
			return super(OrdenDeTrabajoCreateView,self).post(request,args,kwargs)

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


class OrdenDeTrabajoUpdateView(LoginRequiredMixin, UpdateView):
	model = OrdenDeTrabajo
	fields = fields = [
	'sucursal','empleado','cliente',
	'vehiculo','placa','observacion',
	'habilitado']
	success_url = reverse_lazy('orden_de_trabajo:listar')
	template_name = 'orden_de_trabajo/form.html'

	def get_context_data(self,**kwargs):
		context = super(OrdenDeTrabajoUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Orden de Trabajo'
		context['vehiculos'] = Vehiculo.objects.all()
		context['clientes'] = Cliente.objects.all()
		return context
