# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Cliente
from apps.inicio.mixins import LoginRequiredMixin

class ListaClientes(LoginRequiredMixin,ListView):
	model = Cliente
	context_object_name = 'lista_clientes'
	template_name = "cliente/list.html"

class ClienteDetailView(LoginRequiredMixin,DetailView):
	model = Cliente
	context_object_name = 'cliente'
	template_name = 'cliente/detalle.html'
