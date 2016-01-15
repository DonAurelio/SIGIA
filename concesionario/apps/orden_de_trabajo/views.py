# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from .models import OrdenDeTrabajo
from .models import COTIZADO
from apps.sucursal.models import Sucursal

class OrdenDeTrabajoListView(ListView):
	model = OrdenDeTrabajo
	context_object_name = 'ordenes_de_trabajo'
	template_name = 'orden_de_trabajo/list.html'

	def get_queryset(self):
		sucursal = Sucursal.objects.get(id=self.kwargs['spk'])
		return OrdenDeTrabajo.objects.filter(sucursal=sucursal).exclude(estado_reparacion=COTIZADO)




