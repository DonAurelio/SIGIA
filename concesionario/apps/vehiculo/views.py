# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Vehiculo 

class ListaVehiculos(ListView): 
	model = Vehiculo
	context_object_name = 'lista_vehiculos'