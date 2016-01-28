# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo
from apps.orden_de_trabajo.models import REPARADO
from .models import FacturaOrdenDeTrabajo
from apps.sucursal.models import SucursalRepuesto
from apps.cotizacion_orden_de_trabajo.models import RepuestoCantidad

class FacturaOrdenDeTrabajoCreateView(TemplateView):

    def get(self,request,*args,**kwargs):
        context = {}
        cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])

        if cotizacion.es_valida():
            info_repuestos_faltantes = self.verificar_inventario_sucursal(cotizacion)
            if info_repuestos_faltantes:
                messages.info(request,'No es posible reparar el vehiculo en este momento')
                for info in info_repuestos_faltantes:
                    messages.info(request,info)
                return HttpResponseRedirect(reverse_lazy('orden_de_trabajo:listar'))
            else:
                cotizacion.orden_de_trabajo.estado_reparacion = REPARADO
                cotizacion.orden_de_trabajo.save()

                factura = FacturaOrdenDeTrabajo(
                    cotizacion=cotizacion,
                    costo_total=cotizacion.costo_total()
                )
                factura.save()

                repuestos_cantidad = RepuestoCantidad.objects.filter(
                    cotizacion_orden_de_trabajo=cotizacion
                )

                context={ 'factura':factura }

                return render_to_response(
                    'factura_orden_de_trabajo/form.html',
                    context,
                    context_instance=RequestContext(request)
                )

        else:
            messages.info(request,'La cotización esta vencida, debe actualizarla para efectuar la reparacion')
            context = {'modal_messages':True}
            return HttpResponseRedirect(reverse_lazy('orden_de_trabajo:listar'))


    def verificar_inventario_sucursal(self,cotizacion):
        """ Documentacion verificar_inventario_sucursal

            Dada una cotizacion y una sucursal, determina si la sucursal cuenta
            con la cantidad de repuestos necesarios en el inventario, de no ser
            asi, retorna una lista donde cada item indica, el nombre del repuesto
            y las unidades faltantes.

            Atributos:
                cotizacion (CotizacionOrdenDeTrabajo):

        """

        # Obtenemos la sucursal implicada en la cotizacion de la orden de trabajo
        sucursal = cotizacion.orden_de_trabajo.sucursal

        # Obtenemos cada uno de los repuestos de la cotizacion y comparamos las
        # cantidades con las unidades existente en la sucursal, para determinar
        # si en el inventario de la sucursal hay la cantidad de cada repuesto
        # necesaria para reparar el vehiculo y efectuar lo facturacion

        # En caso de que no haya la cantidad necesaria de un repuesto, se coloca en una lista
        # para reportar al usuario por medio de un mensaje

        info_repuestos_faltantes = []
        # Obtenemos los repuestos que estan ligados a una determinada cotizacion de orden de trabajo
        # luego se comparan con la cantidad de repuestos en el inventario de la sucursal

        for cotizacion_repuesto in cotizacion.repuestos_cantidad.all():
            try:
                sucursal_repuesto = SucursalRepuesto.objects.filter(
                    sucursal=sucursal,
                    repuesto=cotizacion_repuesto.repuesto
                )[0]
                if cotizacion_repuesto.cantidad > sucursal_repuesto.cantidad:
                    nombre_repuesto = cotizacion_repuesto.repuesto.nombre
                    unidades_faltantes = cotizacion_repuesto.cantidad - sucursal_repuesto.cantidad
                    info_repuestos_faltantes.append("Faltan {} unidades de \t {}".format(unidades_faltantes,nombre_repuesto))
            except IndexError:
                info_repuestos_faltantes.append(
                "EL repuesto {} no esta disponible en esta sucursal".format(cotizacion_repuesto.repuesto.nombre))


        if info_repuestos_faltantes == []:
            return None
        else:
            return info_repuestos_faltantes
