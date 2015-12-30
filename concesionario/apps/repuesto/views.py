# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Repuesto 

class RepuestosSucursalListView(ListView): 
	"""Lista los repuestos por sucursal. """
	
	model = Repuesto
	context_object_name = 'lista_repuestos'

	def get_queryset(self):
		"""Obtiene la pk de la sucursal por url


		Dala la pk de la sucursal se sobre escribe el metodo
		para que se listen los repuestos que pertenecen a una
		sucursal dada.

		"""
		sucursal_id = self.kwargs['pk']
		return Repuesto.objects.filter(sucursal_id=sucursal_id)

class RepuestosListView(ListView):

	model = Repuesto
	context_object_name = 'repuestos'
