# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Venta
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
  
class CrearVenta(CreateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'descuento', 'precio_venta', 'forma_pago']
    success_url = reverse_lazy('venta:listar')
 
    def get_context_data(self,**kwargs):
     	context = super(CrearVenta,self).get_context_data(**kwargs)
     	context['search_button_text'] = 'Completar Formulario'
     	clientes = Cliente.objects.all()
     	context['lista_clientes'] = clientes
     	vehiculos = Vehiculo.objects.all()
     	context['vehiculos'] = vehiculos
     	return context

    def get_initial(self):
        initial = super(CrearVenta,self).get_initial()
        initial = initial.copy()
        initial['empleado'] = Empleado.objects.get(user_id=self.request.user.id)
        return initial

class ActualizarVenta(UpdateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'descuento', 'precio_venta', 'forma_pago']
    success_url = reverse_lazy('venta:listar')  