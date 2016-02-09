# -*- encoding: utf-8 -*-

from django.views.generic.list import ListView
from .models import FacturaOrdenDeTrabajo
from apps.sucursal.models import Sucursal

class FacturaOrdenDeTrabajoListView(ListView):

	model = FacturaOrdenDeTrabajo
	template_name = 'factura_orden_de_trabajo/list.html'
	context_object_name = 'facturas'

	def get_queryset(self):
		query = super(FacturaOrdenDeTrabajoListView,self).get_queryset()
		return query.filter(cotizacion__orden_de_trabajo__sucursal__id=self.kwargs['pk'])

	def get_context_data(self,**kwargs):
		context = super(FacturaOrdenDeTrabajoListView,self).get_context_data(**kwargs)
		context['sucursal'] = Sucursal.objects.get(id=self.kwargs['pk'])
		return context



