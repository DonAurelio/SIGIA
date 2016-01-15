# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from .models import OrdenDeTrabajo
from .models import COTIZADO
from apps.sucursal.models import Sucursal
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo

class OrdenDeTrabajoListView(ListView):
	model = OrdenDeTrabajo
	context_object_name = 'ordenes_de_trabajo'
	template_name = 'orden_de_trabajo/list.html'

	def get_queryset(self):
		sucursal = Sucursal.objects.get(id=self.request.user.empleado.sucursal.id)
		return OrdenDeTrabajo.objects.filter(sucursal=sucursal).exclude(estado_reparacion=COTIZADO)

	def get_context_data(self):
		context = super(OrdenDeTrabajoListView,self).get_context_data()
		sucursal = Sucursal.objects.get(id=self.request.user.empleado.sucursal.id)
		context['cotizaciones_ordenes_de_trabajo'] = CotizacionOrdenDeTrabajo.objects.filter(orden_de_trabajo__sucursal=sucursal)
		return context




