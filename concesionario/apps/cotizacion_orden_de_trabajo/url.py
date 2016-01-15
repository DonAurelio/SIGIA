# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .forms import CotizacionOrdenDeTrabajoCreateView

urlpatterns = [
	url(r'^cotizacion/orden_de_trabajo/crear/(?P<opk>\d+)/$',CotizacionOrdenDeTrabajoCreateView.as_view(),name='crear'),
]