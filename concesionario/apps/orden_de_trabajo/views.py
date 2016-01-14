# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from .models import OrdenDeTrabajo

class OrdenDeTrabajoListView(ListView):
	model = OrdenDeTrabajo
	context_object_name = 'ordenes_de_trabajo'
	template_name = 'orden_de_trabajo/list.html'


