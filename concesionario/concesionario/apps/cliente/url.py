from django.conf.urls import include, url
from concesionario.apps.cliente.forms import CrearCliente

urlpatterns = [
	url(r'^cliente/crear$', CrearCliente.as_view(), name='crear'),	
]