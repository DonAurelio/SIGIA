# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Repuesto 

class ListaRepuestos(ListView): 
	model = Repuesto
	context_object_name = 'lista_repuestos'