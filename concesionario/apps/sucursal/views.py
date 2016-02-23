# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Sucursal
from .forms import SucursalCreateForm
from apps.inicio.mixins import LoginRequiredMixin

class SucursalesListView(LoginRequiredMixin, ListView): 
	"""Lista todas las sucursales de la base de datos."""
	model = Sucursal
	context_object_name = 'sucursales'
	template_name = 'sucursal/list.html'

	def get_context_data(self,**kwargs):
		context = super(SucursalesListView,self).get_context_data(**kwargs)
		return context
