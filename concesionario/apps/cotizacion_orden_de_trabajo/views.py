# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext

from apps.sucursal.models import Sucursal
from .models import CotizacionOrdenDeTrabajo

class CotizacionOrdenDeTrabajoDetailView(TemplateView):

	def get(self,request,*args,**kwargs):
		cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])
		context = { 'cotizacion':cotizacion }

		return render_to_response(
				'cotizacion_orden_de_trabajo/detalle.html',
				context,
				context_instance = RequestContext(request)
			)

class CotizacionOrdenDeTrabajoListView(TemplateView):

	def get(self,request,*args,**kwargs):
		sucursal = Sucursal.objects.get(id=kwargs['pk'])
		cotizaciones = CotizacionOrdenDeTrabajo.objects.filter(
			orden_de_trabajo__sucursal = sucursal
			)

		context = {
			'sucursal':sucursal, 
			'cotizaciones':cotizaciones
		 }
		return render_to_response(
			'cotizacion_orden_de_trabajo/list.html',
			context,
			context_instance = RequestContext(request) )





