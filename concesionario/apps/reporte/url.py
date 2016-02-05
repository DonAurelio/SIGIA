# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import ReporteVendedores

urlpatterns = [
	url(r'^reporte/MejoresVendedores/$',ReporteVendedores.as_view(), name='MejoresVendedores'),]
