# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import CrearRepuesto
from .forms import ActualizarRepuesto
from .views import RepuestosSucursalListView
from .views import RepuestosListView

from .forms import RepuestoSucursalAjaxCreateView
from .forms import RepuestoSucursalUpdateView
from .views import RepuestoSucursalListView

urlpatterns = [

    url(r'^repuesto/crear$', CrearRepuesto.as_view(), name='crear'),
    url(r'^repuesto/(?P<pk>\d+)/$', ActualizarRepuesto.as_view(), name='actualizar'),
    url(r'^repuestos/$', RepuestosListView.as_view(), name='listar'),

    url(r'^repuestos/sucursal/(?P<spk>\d+)/agregar/(?P<rpk>\d+)/$', RepuestoSucursalAjaxCreateView.as_view(), name='agregar-repuesto-sucursal'),
    url(r'^repuestos/sucursal/actualizar/(?P<pk>\d+)/$', RepuestoSucursalUpdateView.as_view(), name='actualizar-repuesto-sucursal'),
    url(r'^repuestos/sucursal/(?P<pk>\d+)/$', RepuestoSucursalListView.as_view(), name='listar-repuestos-sucursal'),
]
