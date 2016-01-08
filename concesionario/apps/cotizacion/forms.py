# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Cotizacion 
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
 
  
class CrearCotizacion(CreateView): 

    model = Cotizacion 
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha_vencimiento', 'forma_pago'] 
    readonly_fields = ['empleado', 'cliente', 'vehiculo']
    success_url = reverse_lazy('cotizacion:listar') 


    def get_context_data(self,**kwargs):
        context = super(CrearCotizacion,self).get_context_data(**kwargs)
        # context['section_title'] = 'Vehículos Disponibles'
        # context['submit_button_text'] = 'Agregar'
        context['search_button_text'] = 'Completar Formulario'
        
        # Vehiculos que no estan en la sucursal con id = self.kwargs['pk']
        #vehiculos = Vehiculo.objects.exclude(sucursalvehiculo__sucursal__id=self.kwargs['pk'])
        clientes = Cliente.objects.all()
        context['lista_clientes'] = clientes

        vehiculos = Vehiculo.objects.all()
        context['vehiculos'] = vehiculos
        
        return context

    def get_initial(self):
        initial = super(CrearCotizacion,self).get_initial()
        initial = initial.copy()
        initial['empleado'] = Empleado.objects.get(user_id=self.request.user.id)
        return initial

    def get_success_url(self):
        return reverse_lazy('cotizacion:listar')


class ActualizarCotizacion(UpdateView): 
    model = Cotizacion 
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha','fecha_vencimiento', 'forma_pago'] 
    success_url = reverse_lazy('cotizacion:listar') 
    