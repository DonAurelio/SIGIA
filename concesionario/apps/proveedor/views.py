from django.shortcuts import render
from django.views.generic import ListView
from .models import Proveedor

class ProveedorListView(ListView):

	model = Proveedor
	context_object_name = 'proveedores'
	template_name = 'proveedor/list.html'
