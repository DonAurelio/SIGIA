from django.shortcuts import render
from django.views.generic import ListView
from .models import Proveedor
from apps.inicio.mixins import LoginRequiredMixin

class ProveedorListView(LoginRequiredMixin, ListView):

	model = Proveedor
	context_object_name = 'proveedores'
	template_name = 'proveedor/list.html'
