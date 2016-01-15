# -*- encoding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import CotizacionOrdenDeTrabajo
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.orden_de_trabajo.models import COTIZADO

class CotizacionOrdenDeTrabajoCreateView(CreateView):
    model = CotizacionOrdenDeTrabajo
    fields = ['orden_de_trabajo','repuestos','detalles','costo','fecha_vencimiento']
    template_name = 'cotizacion_orden_de_trabajo/form.html'

    def get_context_data(self,**kwargs):
        context = super(CotizacionOrdenDeTrabajoCreateView,self).get_context_data(**kwargs)
        context['section_title'] = 'Nueva Cotización'
        return context

    def get_initial(self):
        initial = super(CotizacionOrdenDeTrabajoCreateView,self).get_initial()
        initial = initial.copy()
        orden_de_trabajo = OrdenDeTrabajo.objects.get(id=self.kwargs['opk'])
        initial['orden_de_trabajo'] = orden_de_trabajo
        return initial

    def get_success_url(self):
        orden_de_trabajo = OrdenDeTrabajo.objects.get(id=self.kwargs['opk'])
        sucursal_id = orden_de_trabajo.sucursal.id
        cotizacion_orden_de_trabajo = CotizacionOrdenDeTrabajo.objects.get(id=self.object.id)
        cotizacion_orden_de_trabajo.orden_de_trabajo.estado_reparacion = COTIZADO
        cotizacion_orden_de_trabajo.save()
        return reverse_lazy('orden_de_trabajo:listar',kwargs={'spk':sucursal_id})
