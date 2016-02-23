# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.inicio.mixins import LoginRequiredMixin
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo
from apps.orden_de_trabajo.models import REPARADO
from .models import FacturaOrdenDeTrabajo
from apps.sucursal.models import SucursalRepuesto
from apps.cotizacion_orden_de_trabajo.models import RepuestoCantidad

class FacturaOrdenDeTrabajoCreateView(LoginRequiredMixin, TemplateView):

    def get(self,request,*args,**kwargs):
        """ Documentacion get

            Permite generar la factura que es el paso siguiente a una cotización
            de una orden de trabajo, antes de generarse la factura, se comprueba
            si la cotización no esta vencida, luego se verifica que en inventario
            de la sucursal esten todos los repuestos necesarios para reparar el
            vehiculo, luego se hace el descuento de las unidades del inventario
            de la sucursal. Finalmente se muestra la factura.

        """

        context = {}
        cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])

        # S e verifica si la cotizacion esta vencida
        if cotizacion.es_valida():

            # Verificacion de repuestos faltantes
            info_repuestos_faltantes = self.verificar_inventario_sucursal(cotizacion)

            # Si faltan repuestos, se cargan los repuestso faltantes en django.contrib.messages
            if info_repuestos_faltantes:
                self.cargar_mensajes_de_errores(info_repuestos_faltantes)
                return HttpResponseRedirect(reverse_lazy('orden_de_trabajo:listar'))

            # Si todos los repuestos estan disponibles, se hace el descuento de los repuestos
            # Si hay algun errorr se carga en django.contrib.message
            errores = []
            errores = self.descontar_repuestos_inventario_sucursal(cotizacion)

            if errores:
                self.cargar_mensajes_de_errores(errores)
                return HttpResponseRedirect(reverse_lazy('orden_de_trabajo:listar'))


            # Si no hay errores, se coloca el estado de la cotizacion del vehiculo como REPARADO
            cotizacion.orden_de_trabajo.estado_reparacion = REPARADO
            cotizacion.orden_de_trabajo.save()

            # Se crea la factura
            factura = FacturaOrdenDeTrabajo( cotizacion=cotizacion )
            factura.save()

            # Se incluye la factuar en el contexto para ser visualizada
            context={ 'factura':factura }

            return render_to_response(
                'factura_orden_de_trabajo/detalle.html',
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

        return info_repuestos_faltantes

    def descontar_repuestos_inventario_sucursal(self,cotizacion):
        """ Documentacion descontar_repuestos_inventario_sucursal

            Dada una cotizacion, permite descontar del inventario de la sucursal
            la cantidad de repuestos especificados en la cotizacion.

        """
        # Errores
        errores = []

        # Obtenemos la sucursal de la cual se hara el descuento en el inventario
        sucursal = cotizacion.orden_de_trabajo.sucursal

        # Hacemos un recorrdio por los repuestos_cantidad que hay en la cotizacion
        for cotizacion_repuesto in cotizacion.repuestos_cantidad.all():
            try:
                sucursal_repuesto = SucursalRepuesto.objects.filter(
                    sucursal=sucursal,
                    repuesto=cotizacion_repuesto.repuesto
                )[0]

                sucursal_repuesto.cantidad = sucursal_repuesto.cantidad - cotizacion_repuesto.cantidad
                sucursal_repuesto.save()

            except IndexError:
                errores.append(
                "Se prento un error al consultar el repuesto {} no esta disponible en esta sucursal".format(
                    cotizacion_repuesto.repuesto.nombre))

        return errores

    def cargar_mensajes_de_errores(self,errores):
        """
            Documentacion cargar_mensajes_de_errores

            Permite cargar una lista de errores a django.contrib.messages
            para que sean visualizados en el template.

        """

        messages.info(self.request,'No es posible reparar el vehiculo en este momento')
        for info in errores:
            messages.info(self.request,info)


class FacturaOrdenDeTrabajoDetailView(LoginRequiredMixin, TemplateView):

    def get(self,request,*args,**kwargs):
        """
            Documentacion get

            Permite visualizar una factura dada su identificacíon.
        """
        factura = FacturaOrdenDeTrabajo.objects.get(id=kwargs['pk'])
        context = {'factura':factura}
        return render_to_response(
            'factura_orden_de_trabajo/detalle.html',
            context,
            context_instance=RequestContext(request))
