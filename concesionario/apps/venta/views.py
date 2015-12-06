# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Venta 

class ListaVentas(ListView): 
	model = Venta
	context_object_name = 'lista_ventas'