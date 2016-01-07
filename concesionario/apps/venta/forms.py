# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Venta
 
class CrearVenta(CreateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha_venta', 'descuento', 'precio_venta', 'forma_pago']
    success_url = reverse_lazy('venta:listar') 
class ActualizarVenta(UpdateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha_venta', 'descuento', 'precio_venta', 'forma_pago']
    success_url = reverse_lazy('venta:listar') 