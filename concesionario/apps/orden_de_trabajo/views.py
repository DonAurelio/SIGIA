# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import OrdenDeTrabajo
from .models import PENDIENTE
from .models import COTIZADO
from .models import REPARADO
from .models import RETIRADO
from .models import REPARADO_Y_ENTREGADO
from .models import OrdenDeTrabajo
from apps.sucursal.models import Sucursal
from apps.empleado.models import Empleado
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo
from apps.factura_orden_de_trabajo.models import FacturaOrdenDeTrabajo
from datetime import datetime

class OrdenDeTrabajoListView(ListView):
	model = OrdenDeTrabajo
	context_object_name = 'ordenes_de_trabajo'
	template_name = 'orden_de_trabajo/list.html'

	def get_queryset(self):
		empleado = Empleado.objects.get(id=self.request.user.empleado.id)
		return OrdenDeTrabajo.objects.filter(empleado=empleado,estado_reparacion=PENDIENTE)

	def get_context_data(self):
		context = super(OrdenDeTrabajoListView,self).get_context_data()
		empleado = Empleado.objects.get(id=self.request.user.empleado.id)

		# Se listan las cotizaciones de las ordenes de trabajo, con el fin de mostrar
		# en el template las ordenes de trabajo cuyas repeparaciones han sido cotizadas
		context['cotizaciones'] = CotizacionOrdenDeTrabajo.objects.filter(
			orden_de_trabajo__empleado=empleado,
			orden_de_trabajo__estado_reparacion=COTIZADO
		)

		# Se listan las facturas de las ordenes de trabajo, con el fin de mostrar
		# en el template las ordenes de trabajo facturadas
		context['facturas'] = FacturaOrdenDeTrabajo.objects.filter(
			cotizacion__orden_de_trabajo__empleado=empleado,
			cotizacion__orden_de_trabajo__estado_reparacion=REPARADO
		)

		# Se listan las ordenes de trabajo que han sido realizadas y cuyos vehiculos
		# han sido entregados a sus respectivos clientes
		context['reparados_entregados'] = OrdenDeTrabajo.objects.filter(
			empleado=empleado,
			estado_reparacion=REPARADO_Y_ENTREGADO
		)

		# Se listan las ordenes de trabajo que cuya reparacion no fue efectuada
		# ya que el cliente retiro el vehiuclo
		context['retirados'] = OrdenDeTrabajo.objects.filter(
			empleado=empleado,
			estado_reparacion=RETIRADO
		)
		return context


class RetirarEntregarVehiculoTemplateView(TemplateView):

	def get(self,request,*args,**kwargs):
		orden_de_trabajo = OrdenDeTrabajo.objects.get(id=kwargs['pk'])
		try:
			# Si la orden de trabajo, no tiene cotizacion o
			# si tiene cotziacion y no tiene factura, se genera
			# una exepcion al hacer el siguiente llamado
			# orden_de_trabajo.cotizacion.factura
			orden_de_trabajo.cotizacion.factura

			# En el caso de que no se lance la excepcion entonces el
			# vehiculo tiene cotizacion y factura, por lo tanto ya fue
			# reparado y se cambia el estado de la cotizacion a
			# REPARADO_Y_ENTREGADO al momento de ser retirado
			orden_de_trabajo.estado_reparacion = REPARADO_Y_ENTREGADO
			messages.info(request,'El vehiculo fue entregado con exito')
		except ObjectDoesNotExist:
			orden_de_trabajo.estado_reparacion = RETIRADO
			messages.info(request,'El vehiculo fue retirado con exito')

		orden_de_trabajo.fecha_salida = datetime.now().date()
		orden_de_trabajo.save()

		return HttpResponseRedirect(reverse_lazy('orden_de_trabajo:listar'))
