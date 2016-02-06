# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import ReporteVendedores
from .forms import ReporteVentasSucursal
from .forms import ReporteGananciasSucursal
from .forms import ReporteVehiculosSucursal
from .forms import ReporteProveedoresUsados
from .forms import ReporteSucursalRepuestos


urlpatterns = [
	url(r'^reporte/MejoresVendedores/$',ReporteVendedores.as_view(), name='MejoresVendedores'),
	url(r'^reporte/VentasSucursal/$',ReporteVentasSucursal.as_view(), name='VentasSucursal'),
	url(r'^reporte/GananciasSucursal/$',ReporteGananciasSucursal.as_view(), name='GananciasSucursal'),
	url(r'^reporte/VehiculosSucursal/$',ReporteVehiculosSucursal.as_view(), name='VehiculosSucursal'),
	url(r'^reporte/ProveedoresUsados/$',ReporteProveedoresUsados.as_view(), name='ProveedoresUsados'),
	url(r'^reporte/SucursalRepuestos/$',ReporteSucursalRepuestos.as_view(), name='SucursalRepuestos'),

	]
