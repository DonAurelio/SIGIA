# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Sucursal 

class ListaSucursales(ListView): 
	"""Lista todas las sucursales de la base de datos."""
	
	model = Sucursal
	context_object_name = 'lista_sucursales'