# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from .models import Venta
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from apps.inicio.mixins import LoginRequiredMixin

class ListaVentas(LoginRequiredMixin, ListView):
	model = Venta
	context_object_name = 'lista_ventas'


class FacturaCreateView(LoginRequiredMixin, TemplateView):
	def get(self,request,*args,**kwargs):
		venta= Venta.objects.get(id=kwargs['pk'])
		context = {'venta':venta}

		return render_to_response(
			'venta/factura.html',
			context,
			context_instance=RequestContext(request)
		)
