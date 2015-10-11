# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearCliente

urlpatterns = [
	url(r'^cliente/crear$', CrearCliente.as_view(), name='crear'),	
]