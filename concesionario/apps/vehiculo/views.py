# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from django.views.generic.detail import DetailView 
from .models import Vehiculo 

class ListaVehiculosSucursal(ListView): 
	"""Lista los vehiculos por sucursal."""
	
	model = Vehiculo
	context_object_name = 'lista_vehiculos'

	def get_queryset(self):
		'''Obtiene la pk de la sucursal por url

		Dada la pk de la sucursal se sobre escribe el metodo
		para que se listen los vehiculos que pertenecen a una
		sucursal dada.

		'''
		sucursal_id = self.kwargs['pk']
		return Vehiculo.objects.filter(sucursal_id=sucursal_id)