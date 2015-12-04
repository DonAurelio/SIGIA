# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Vehiculo
 
class CrearVehiculo(CreateView):
    model = Vehiculo
    fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
    'capacidad', 'caracteristicas', 'imagen', 'precio', 'sucursal']

class ActualizarVehiculo(UpdateView):
    model = Vehiculo 
    fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
    'capacidad', 'caracteristicas', 'imagen', 'precio', 'sucursal']