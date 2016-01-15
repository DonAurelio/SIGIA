# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Venta
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
from apps.sucursal.models import SucursalVehiculo
  
class CrearVenta(CreateView):
    model = Venta
    #precio_venta: no se incluye este campo en el formulario pero
    fields = ['cliente', 'sucursal_vehiculo', 'forma_pago']
    success_url = reverse_lazy('venta:listar')
 
    def get_context_data(self,**kwargs):
     	# empleado logueado
        empleado = Empleado.objects.get(user_id=self.request.user.id)
        # sucursal del empleado
        sucursal = empleado.sucursal
        context = super(CrearVenta,self).get_context_data(**kwargs)
     	context['search_button_text'] = 'Completar Formulario'
     	clientes = Cliente.objects.all()
     	context['lista_clientes'] = clientes

        sucursal_vehiculo = SucursalVehiculo.objects.filter(sucursal=sucursal)
        context['sucursal_vehiculos'] = sucursal_vehiculo
        return context

    def post(self, request, *args, **kwargs):
        
        empleado = Empleado.objects.get(user_id=self.request.user.id)
        cliente = Cliente.objects.get(pk=request.POST["cliente"])
        sucursal_vehiculo = SucursalVehiculo.objects.get(pk=request.POST["sucursal_vehiculo"])
        forma_pago = request.POST["forma_pago"]
        venta = Venta(empleado = empleado, cliente = cliente, sucursal_vehiculo = sucursal_vehiculo,
            precio_venta = sucursal_vehiculo.vehiculo.precio, forma_pago = forma_pago)
        venta.save()
        
        sucursal_vehiculo.cantidad = sucursal_vehiculo.cantidad-1
        sucursal_vehiculo.save()

        return HttpResponseRedirect(reverse_lazy('venta:listar') )

class ActualizarVenta(UpdateView):
    model = Venta
    fields = ['empleado', 'cliente', 'vehiculo', 'precio_venta', 'forma_pago']
    success_url = reverse_lazy('venta:listar')  