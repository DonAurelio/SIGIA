# -*- encoding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Sucursal
 
class CrearSucursal(CreateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
    success_url = reverse_lazy('sucursal:listar') 

   
class ActualizarSucursal(UpdateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad','habilitado']
    success_url = reverse_lazy('sucursal:listar') 