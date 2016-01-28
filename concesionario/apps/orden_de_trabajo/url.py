# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .forms import OrdenDeTrabajoCreateView
from .forms import OrdenDeTrabajoUpdateView
from .views import OrdenDeTrabajoListView
from .views import RetirarEntregarVehiculoTemplateView

urlpatterns = [
	url(r'^orden_de_trabajo/crear/$',OrdenDeTrabajoCreateView.as_view(),name='crear'),
	url(r'^orden_de_trabajo/(?P<pk>\d+)/$',OrdenDeTrabajoUpdateView.as_view(),name='actualizar'),
	url(r'^orden_de_trabajo/listado/',OrdenDeTrabajoListView.as_view(),name='listar'),
	url(r'^orden_de_trabajo/retirar/entregar/(?P<pk>\d+)/',RetirarEntregarVehiculoTemplateView.as_view(),name='entregar-retirar-vehiculo')
]
