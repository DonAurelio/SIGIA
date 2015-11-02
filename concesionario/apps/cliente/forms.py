# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Cliente

# Crea el registro de un cliente mediante la clase generica CreateView
class CrearCliente(CreateView):
	model = Cliente
	fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
	'departamento', 'telefono', 'celular', 'email']

class ActualizarCliente(UpdateView): 
    model = Cliente 
    fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
    'departamento', 'telefono', 'celular', 'email']