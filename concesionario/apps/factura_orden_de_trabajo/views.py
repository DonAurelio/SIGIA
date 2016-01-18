from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo
from apps.orden_de_trabajo.models import REPARADO
from .models import FacturaOrdenDeTrabajo

class FacturaOrdenDeTrabajoCreateView(TemplateView):

    def get(self,request,*args,**kwargs):
        cotizacion = CotizacionOrdenDeTrabajo.objects.get(id=kwargs['pk'])
        cotizacion.orden_de_trabajo.estado_reparacion = REPARADO
        cotizacion.orden_de_trabajo.save()
        costo_total_respuestos = 0
        for repuesto in cotizacion.repuestos.all():
            costo_total_respuestos += repuesto.precio

        costo_total_reparacion = costo_total_respuestos + cotizacion.costo
        context = {
            'costo_total_respuestos':costo_total_respuestos,
            'costo_total_reparacion':costo_total_reparacion
        }

        return render_to_response(
            'factura_orden_de_trabajo/form.html',
            context,
            context_instance=RequestContext(request)
        )
