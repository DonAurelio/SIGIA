# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Sucursal 

class ListaSucursales(ListView): 
	model = Sucursal
	context_object_name = 'lista_sucursales'