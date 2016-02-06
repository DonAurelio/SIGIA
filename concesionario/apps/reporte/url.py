# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import ReporteVendedores
from .forms import ReporteVentasSucursal
from .forms import ReporteGananciasSucursal
from .forms import ReporteVehiculosSucursal
urlpatterns = [
	url(r'^reporte/MejoresVendedores/$',ReporteVendedores.as_view(), name='MejoresVendedores'),
	url(r'^reporte/VentasSucursal/$',ReporteVentasSucursal.as_view(), name='VentasSucursal'),
	url(r'^reporte/GananciasSucursal/$',ReporteGananciasSucursal.as_view(), name='GananciasSucursal'),
	url(r'^reporte/VehiculosSucursal/$',ReporteVehiculosSucursal.as_view(), name='VehiculosSucursal'),

	]
