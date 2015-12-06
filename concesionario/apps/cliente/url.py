# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearCliente, ActualizarCliente
from .views import ListaClientes

urlpatterns = [
	#url que redirecciona a la pagina de creacion de clientes
	url(r'^cliente/crear$', CrearCliente.as_view(), name='crear'),	
	url(r'^cliente/(?P<pk>\d+)/$', ActualizarCliente.as_view(), name='actualizar'),
	url(r'^cliente/listado$', ListaClientes.as_view(), name='listar'),
]