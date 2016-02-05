# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import ReporteVendedores
from .forms import ReporteVentasSucursal

urlpatterns = [
	url(r'^reporte/MejoresVendedores/$',ReporteVendedores.as_view(), name='MejoresVendedores'),
	url(r'^reporte/VentasSucursal/$',ReporteVentasSucursal.as_view(), name='VentasSucursal'),

	]
