# -*- encoding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from .models import CotizacionOrdenDeTrabajo
from .models import RepuestoCantidad
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.orden_de_trabajo.models import COTIZADO
from django.forms import inlineformset_factory
from django.forms import ModelForm

class CotizacionOrdenDeTrabajoForm(ModelForm):
    class Meta:
        model = CotizacionOrdenDeTrabajo
        exclude = ('habilitado',)

class RepuestoCantidadForm(ModelForm):
    class Meta:
        model = RepuestoCantidad
        fields = ('cotizacion_orden_de_trabajo','repuesto','cantidad')

RepuestoCantidadFormSet = inlineformset_factory(
    CotizacionOrdenDeTrabajo,
    RepuestoCantidad,
    fields=('repuesto','cantidad'),
    extra=2)

class CotizacionOrdenDeTrabajoCreateView(CreateView):
    model = CotizacionOrdenDeTrabajo
    form_class = CotizacionOrdenDeTrabajoForm
    template_name = 'cotizacion_orden_de_trabajo/form.html'

    def get_context_data(self,**kwargs):
        context = super(CotizacionOrdenDeTrabajoCreateView,self).get_context_data(**kwargs)
        context['section_title'] = 'Nueva Cotización'
        if self.request.POST:
            context['formset'] = RepuestoCantidadFormSet(self.request.POST)
        else:
            context['formset'] = RepuestoCantidadFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )

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
        cotizacion_orden_de_trabajo.orden_de_trabajo.save()
        return reverse_lazy('orden_de_trabajo:listar')

class CotizacionOrdenDeTrabajoUpdateView(UpdateView):
    model = CotizacionOrdenDeTrabajo
    fields = ['orden_de_trabajo','repuestos','detalles','costo','fecha_vencimiento']
    template_name = 'cotizacion_orden_de_trabajo/form.html'
    success_url = reverse_lazy('orden_de_trabajo:listar')

    def get_context_data(self,**kwargs):
        context = super(CotizacionOrdenDeTrabajoUpdateView,self).get_context_data(**kwargs)
        context['section_title'] = 'Actualizar Cotización'
        return context
