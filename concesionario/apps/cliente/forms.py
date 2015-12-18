# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Cliente

# Crea el registro de un cliente mediante la clase generica CreateView
class CrearCliente(CreateView):
	model = Cliente
	fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
	'departamento', 'telefono', 'celular', 'email']
	success_url = reverse_lazy('cliente:listar') 

class ActualizarCliente(UpdateView): 
    model = Cliente 
    fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
    'departamento', 'telefono', 'celular', 'email']
    success_url = reverse_lazy('cliente:listar')

    # -*- encoding: utf-8 -*-


 
 