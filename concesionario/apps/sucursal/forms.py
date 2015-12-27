# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Sucursal
 
class CrearSucursal(CreateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
    success_url = reverse_lazy('sucursal:listar')

    def get_context_data(self,**kwargs):
    	context = super(CrearSucursal,self).get_context_data(**kwargs)
    	context['section_title'] = 'Nueva Sucursal'
    	context['button_text'] = 'Crear'
    	return context

   
class ActualizarSucursal(UpdateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
    success_url = reverse_lazy('sucursal:listar') 


    def get_context_data(self,**kwargs):
    	context = super(ActualizarSucursal,self).get_context_data(**kwargs)
    	context['section_title'] = 'Actualizar Sucursal'
    	context['button_text'] = 'Actualizar'
    	return context