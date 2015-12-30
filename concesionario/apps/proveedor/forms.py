# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Proveedor

class ProveedorCreateView(CreateView):
	model = Proveedor
	fields = [
	'nombre','direccion','telefono','ciudad',
	'email','habilitado']

	template_name = 'proveedor/parciales/proveedor_form.html'
	success_url = reverse_lazy('proveedor:listar')