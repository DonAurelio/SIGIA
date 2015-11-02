# -*- encoding: utf-8 -*-

from django.views.generic import ListView 
from .models import Cliente

class ListaClientes(ListView): 
	model = Cliente
	context_object_name = 'lista_clientes'