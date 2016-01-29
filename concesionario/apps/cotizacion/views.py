# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Cotizacion
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

class ListaCotizaciones(ListView): 
	model = Cotizacion
	context_object_name = 'lista_cotizaciones'



class PdfCreateView(TemplateView):
	def get(self,request,*args,**kwargs):
		cotizacion= Cotizacion.objects.get(id=kwargs['pk'])
		context = {'cotizacion':cotizacion}

		return render_to_response(
			'cotizacion/cotizacionPDF.html',
			context,
			context_instance=RequestContext(request)
		)