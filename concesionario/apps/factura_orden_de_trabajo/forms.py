from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib import messages
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo
from apps.orden_de_trabajo.models import REPARADO
from .models import FacturaOrdenDeTrabajo
from apps.sucursal.models import SucursalRepuesto
from apps.cotizacion_orden_de_trabajo.models import RepuestoCantidad


class FacturaOrdenDeTrabajoCreateView(TemplateView):

    def get(self,request,*args,**kwargs):
        context = {}

        cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])
        sucursal = cotizacion.orden_de_trabajo.sucursal
        messainfo_repuestos_fantantesge_list = self.check_inventario_sucursal(cotizacion,sucursal)
        if info_repuestos_fantantes:
            messages.error(request,'No fue posible reparara el vehiculo')
            for info in info_repuestos_fantantes:
                messages.info(request,info)
                
            context = {'modal_messages':True}
        else:
            cotizacion.orden_de_trabajo.estado_reparacion = REPARADO
            #cotizacion.orden_de_trabajo.save()

        return render_to_response(
            'factura_orden_de_trabajo/form.html',
            context,
            context_instance=RequestContext(request)
        )

    def check_inventario_sucursal(self,cotizacion,sucursal):
        """ Documentacion check_inventario_sucursal

            Dada una cotizacion y una sucursal, determina si la sucursal cuenta
            con la cantidad de repuestos necesarios en el inventario, de no ser
            asi, retorna una lista donde cada item indica, el nombre del repuesto
            y las unidades faltantes.

            Atributos:
                cotizacion (CotizacionOrdenDeTrabajo):
                sucursal (Sucursal):
        """
        #obtenemos los repuestos listados en la cotizacion
        cotizacion_repuestos = RepuestoCantidad.objects.filter(cotizacion_orden_de_trabajo=cotizacion)

        #Obtenemos cada uno de los repuestos de la cotizacion y comparamos las
        #cantidades con las unidades existente en la sucursal, para determinar
        #si en el inventario de la sucursal hay la cantidad de cada repuesto
        #necesaria para reparar el vehiculo y efectuar lo facturacion

        #En caso de que no haya la cantidad necesaria de un repuesto, se coloca en una lista
        info_repuestos_fantantes = []
        for cotizacion_repuesto in cotizacion_repuestos:
            sucursal_repuesto = SucursalRepuesto.objects.filter(sucursal=sucursal,repuesto=cotizacion_repuesto.repuesto)[0]
            if cotizacion_repuesto.cantidad >= sucursal_repuesto.cantidad:
                nombre_repuesto = cotizacion_repuesto.repuesto.nombre
                unidades_faltantes = cotizacion_repuesto.cantidad - sucursal_repuesto.cantidad
                info_repuestos_fantantes.append("Faltan {} unidades de \t {}".format(unidades_faltantes,nombre_repuesto))

        if repuestos_fantantes == []:
            return None
        else:
            return info_repuestos_fantantes
