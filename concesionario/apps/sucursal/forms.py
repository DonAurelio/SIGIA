# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Sucursal
 
class CrearSucursal(CreateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad']

class ActualizarSucursal(UpdateView):
    model = Sucursal
    fields = ['nombre', 'direccion', 'telefono', 'ciudad']