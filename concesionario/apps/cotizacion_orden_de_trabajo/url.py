# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .forms import CotizacionOrdenDeTrabajoCreateView
from .forms import CotizacionOrdenDeTrabajoUpdateView
from .views import CotizacionOrdenDeTrabajoDetailView
from .views import CotizacionOrdenDeTrabajoListView

urlpatterns = [
	url(r'^cotizacion/orden_de_trabajo/crear/(?P<opk>\d+)/$',CotizacionOrdenDeTrabajoCreateView.as_view(),name='crear'),
	url(r'^cotizacion/orden_de_trabajo/actualizar/(?P<pk>\d+)/$',CotizacionOrdenDeTrabajoUpdateView.as_view(),name='actualizar'),
	url(r'^cotizacion/orden_de_trabajo/detalle/(?P<pk>\d+)/$',CotizacionOrdenDeTrabajoDetailView.as_view(),name='detalle'),
	url(r'^cotizaciones/sucursal/(?P<pk>\d+)/$',CotizacionOrdenDeTrabajoListView.as_view(), name='listar'),
]