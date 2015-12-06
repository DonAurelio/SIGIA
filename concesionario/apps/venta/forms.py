# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Venta
 
class CrearVenta(CreateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha_venta', 'descuento', 'precio_venta', 'forma_pago']

class ActualizarVenta(UpdateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha_venta', 'descuento', 'precio_venta', 'forma_pago']