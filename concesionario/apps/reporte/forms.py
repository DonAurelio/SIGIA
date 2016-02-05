# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
import json
from django.db.models import Count

from django.views.generic import View
from .models import Reporte
from apps.vehiculo.models import Vehiculo
from django.shortcuts import render
from apps.venta.models import Venta
from apps.empleado.models import Empleado
from apps.sucursal.models import Sucursal
from django.db.models.functions import Coalesce

class ReporteVendedores(View):

	
	def get(self, request, **kwargs):

		ventas = Venta.objects.all()
 		
		ventasPorEmpleado =ventas.values("empleado").annotate(cuantos=Count('empleado_id')).order_by(Coalesce('cuantos', 'cuantos').desc())
		for m in ventasPorEmpleado:
			m['empleado'] = str(Empleado.objects.get(id=m["empleado"]).user.first_name)+" "+str(Empleado.objects.get(id=m["empleado"]).user.last_name)+"("+str(Empleado.objects.get(id=m["empleado"]).sucursal)+")"
		print ventasPorEmpleado[1]
		return render (request, 'reporte/reporte_VentasVendedor.html',{'ventasPorEmpleado':ventasPorEmpleado})


class ReporteVentasSucursal(View):

	def get(self, request, **kwargs):
		ventasPorSucursal =Venta.objects.values("empleado__sucursal__nombre").annotate(cuantos=Count('empleado_id')).order_by(Coalesce('cuantos', 'cuantos').desc())
		ventas = []
		for x in range(len(ventasPorSucursal)):
			if x == 0:
				ven = {}
				ven['sucursal']=str(ventasPorSucursal[x]['empleado__sucursal__nombre'])
				ven['cuantos']=ventasPorSucursal[x]['cuantos']
				ventas.append(ven)
			elif ventasPorSucursal[x]['empleado__sucursal__nombre'] == ventasPorSucursal[x-1]['empleado__sucursal__nombre']:
				ventas[x-1]['cuantos']=ventas[x-1]['cuantos']+ventasPorSucursal[x]['cuantos']
			else:
				ven = {}
				ven['sucursal']=str(ventasPorSucursal[x]['empleado__sucursal__nombre'])
				ven['cuantos']=ventasPorSucursal[x]['cuantos']
				ventas.append(ven)

		print ventas
		return render (request, 'reporte/reporte_VentasSucursal.html',{'ventas':ventas})