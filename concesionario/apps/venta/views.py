# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
#from easy_pdf.views import PDFTemplateView
from .models import Venta 

class ListaVentas(ListView): 
	model = Venta
	context_object_name = 'lista_ventas'


#class PDFView(PDFTemplateView):
 #   template_name = "factura.html"



 