# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from .models import Vehiculo
 
class CrearVehiculo(CreateView):
    model = Vehiculo
    fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
    'capacidad', 'caracteristicas', 'imagen', 'precio', 'sucursal']

    #def get_initial(self):

    #def get_success_url(self):
    #	return reverse('')


class ActualizarVehiculo(UpdateView):
    model = Vehiculo 
    fields = ['numero_serie', 'marca', 'modelo', 'motor', 'potencia', 'tipo',
    'capacidad', 'caracteristicas', 'imagen', 'precio', 'sucursal']