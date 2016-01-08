# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Sucursal
from django import forms

class SucursalCreateForm(forms.ModelForm):
	class Meta:
		model = Sucursal
		fields = ('nombre', 'direccion', 'telefono', 'ciudad','habilitado')

class SucursalCreateView(CreateView):
	model = Sucursal
	fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
	template_name = 'sucursal/sucursal_list.html'
	success_url = reverse_lazy('sucursal:listar')

	def get_context_data(self,**kwargs):
		context = super(SucursalCreateView,self).get_context_data(**kwargs)
		context['sucursales'] = Sucursal.objects.all()
		context['form_mode'] = 'create'
		return context

class SucursalUpdateView(UpdateView):
	model = Sucursal
	fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
	success_url = reverse_lazy('sucursal:listar')
	template_name = 'sucursal/sucursal_list.html' 

	def get_context_data(self,**kwargs):
		context = super(SucursalUpdateView,self).get_context_data(**kwargs)
		context['sucursales'] = Sucursal.objects.all()
		context['form_mode'] = 'update'
		return context

