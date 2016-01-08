# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Repuesto 
from .forms import RepuestoSucursalCreateForm
from apps.sucursal.models import Sucursal, SucursalRepuesto


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


class RepuestoSucursalListView(ListView): 
	"""Lista los vehiculos por sucursal."""
	
	model = SucursalRepuesto
	context_object_name = 'sucursal_repuestos'
	template_name = 'repuesto/inventario_list.html'

	def get_queryset(self):
		'''Permite filtrar los vehiculos que seran mostrados.

		Dada la pk de la sucursal se sobre escribe el metodo
		para que se listen los vehiculos que pertenecen a una
		sucursal dada.

		'''

		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		
		sucursal_repuestos = SucursalRepuesto.objects.filter(sucursal=sucursal)
		return sucursal_repuestos

	def get_context_data(self,**kwargs):
		"""Perime agregar al contexto la sucursal a la cual pertenecen los vehiculos listados
		en el query_set."""

		context = super(RepuestoSucursalListView,self).get_context_data(**kwargs)
		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['repuestos'] = Repuesto.objects.all()
		context['form'] = RepuestoSucursalCreateForm()
		context['form_mode'] = 'create'

		return context

