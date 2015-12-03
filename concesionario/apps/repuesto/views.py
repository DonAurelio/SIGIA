# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Repuesto 

class ListaRepuestos(ListView): 
	model = Repuesto
	context_object_name = 'lista_repuestos'