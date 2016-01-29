# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from .models import Cotizacion 
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
  
  
class CrearCotizacion(CreateView): 

    model = Cotizacion 
    fields = [ 'cliente', 'vehiculo', 'fecha_vencimiento', 'forma_pago'] 
    #readonly_fields = ['empleado', 'cliente', 'vehiculo']
    success_url = reverse_lazy('cotizacion:listar') 
 
  
        

    def get_context_data(self,**kwargs):
        
        context = super(CrearCotizacion,self).get_context_data(**kwargs)
        context['search_button_text'] = 'Completar Formulario'
        
        clientes = Cliente.objects.all()
        context['lista_clientes'] = clientes

        vehiculos = Vehiculo.objects.all()
        context['vehiculos'] = vehiculos
        
        return context

    def post(self, request, *args, **kwargs):
        
        empleado = Empleado.objects.get(user_id=self.request.user.id)
        cliente = Cliente.objects.get(pk=request.POST["cliente"])
        vehiculo = Vehiculo.objects.get(pk=request.POST["vehiculo"])
        forma_pago = request.POST["forma_pago"]
        fecha_vencimiento=  request.POST["fecha_vencimiento"]
        print fecha_vencimiento
        cotizacion = Cotizacion(empleado = empleado, cliente = cliente, vehiculo = vehiculo, fecha_vencimiento=fecha_vencimiento,forma_pago = forma_pago)
        cotizacion.save()
        
         
        context = {'cotizacion':cotizacion}
        return render_to_response(
            'cotizacion/cotizacionPDF.html',
            context,
            context_instance=RequestContext(request)
        )


class ActualizarCotizacion(UpdateView): 
    model = Cotizacion 
    fields = ['empleado', 'cliente', 'vehiculo', 'fecha','fecha_vencimiento', 'forma_pago'] 
    success_url = reverse_lazy('cotizacion:listar') 
    