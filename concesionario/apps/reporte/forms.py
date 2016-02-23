# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
import json
from django.db.models import Count, Sum
import random
from django.views.generic import View
from apps.vehiculo.models import Vehiculo
from django.shortcuts import render
from apps.venta.models import Venta
from apps.empleado.models import Empleado
from apps.sucursal.models import Sucursal
from apps.sucursal.models import SucursalVehiculo
from django.db.models.functions import Coalesce
from apps.sucursal.models import SucursalRepuesto
from apps.proveedor.models import Proveedor
from apps.repuesto.models import Repuesto 


class ReporteVendedores(View):

	def get(self, request, **kwargs):
	 
		ventas = Venta.objects.all()
 		
		ventasPorEmpleado =ventas.values("empleado").annotate(cuantos=Count('empleado_id')).order_by(Coalesce('cuantos', 'cuantos').desc())
		for m in ventasPorEmpleado:
			color="#%03x" % random.randint(0, 0xFFF)
			m['empleado'] = str(Empleado.objects.get(id=m["empleado"]).user.first_name)+" "+str(Empleado.objects.get(id=m["empleado"]).user.last_name)+"("+str(Empleado.objects.get(id=m["empleado"]).sucursal)+")"
			m['color']=color
		print ventasPorEmpleado[1]
		return render (request, 'reporte/reporte_VentasVendedor.html',{'ventasPorEmpleado':ventasPorEmpleado})



class ReporteVentasSucursal(View):
	

	def get(self, request, **kwargs):
		levels = range(32,256,32)

		ventasPorSucursal =Venta.objects.values("empleado__sucursal__nombre").annotate(cuantos=Count('empleado_id')).order_by(Coalesce('cuantos', 'cuantos').desc())
		ventas = []
		for x in range(len(ventasPorSucursal)):
			
			if x == 0:
				color="#%03x" % random.randint(0, 0xFFF)
				ven = {}
				ven['sucursal']=str(ventasPorSucursal[x]['empleado__sucursal__nombre'])
				ven['cuantos']=ventasPorSucursal[x]['cuantos']
				ven['color']=color
				ventas.append(ven)
			elif ventasPorSucursal[x]['empleado__sucursal__nombre'] == ventasPorSucursal[x-1]['empleado__sucursal__nombre']:
				ventas[x-1]['cuantos']=ventas[x-1]['cuantos']+ventasPorSucursal[x]['cuantos']
			else:
				color="#%03x" % random.randint(0, 0xFFF)
				ven = {}
				ven['sucursal']=str(ventasPorSucursal[x]['empleado__sucursal__nombre'])
				ven['cuantos']=ventasPorSucursal[x]['cuantos']
				ven['color']=color
				ventas.append(ven)
			#	print color
		#print ventas
		return render (request, 'reporte/reporte_VentasSucursal.html',{'ventas':ventas})


class ReporteGananciasSucursal(View):

	def get(self, request, **kwargs):

		gananciasVentas=Venta.objects.values("empleado__sucursal__nombre").annotate(ganancia=Sum('precio_venta')).order_by(Coalesce('ganancia', 'ganancia').desc())
		ventas = []
		for x in range(len(gananciasVentas)):
			if x == 0:
				ven = {}
				ven['sucursal']=str(gananciasVentas[x]['empleado__sucursal__nombre'])
				ven['ganancia']=gananciasVentas[x]['ganancia']
				ventas.append(ven)
			elif gananciasVentas[x]['empleado__sucursal__nombre'] == gananciasVentas[x-1]['empleado__sucursal__nombre']:
				ventas[x-1]['ganancia']=ventas[x-1]['ganancia']+gananciasVentas[x]['ganancia']
			else:
				ven = {}
				ven['sucursal']=str(gananciasVentas[x]['empleado__sucursal__nombre'])
				ven['ganancia']=gananciasVentas[x]['ganancia']
				ventas.append(ven) 

		print ventas

		return render (request, 'reporte/reporte_GananciasSucursales.html',{'ventas':ventas})

class ReporteVehiculosSucursal(View):

	def get(self, request, **kwargs):
		vehiculos=SucursalVehiculo.objects.values("sucursal__nombre").annotate(cuantos=Sum('cantidad')).order_by(Coalesce('cuantos', 'cuantos').desc())
		
		vehiculo=[]
		for x in range(len(vehiculos)):
			if x == 0:
				veh = {}
				veh['sucursal']=str(vehiculos[x]['sucursal__nombre'])
				veh['cuantos']=vehiculos[x]['cuantos']
				vehiculo.append(veh)
			elif vehiculos[x]['sucursal__nombre'] == vehiculos[x-1]['sucursal__nombre']:
				vehiculo[x-1]['cuantos']=vehiculo[x-1]['cuantos']+vehiculos[x]['cuantos']
			else:
				veh = {}
				veh['sucursal']=str(vehiculos[x]['sucursal__nombre'])
				veh['cuantos']=vehiculos[x]['cuantos']
				vehiculo.append(veh) 
				print vehiculo

		return render (request, 'reporte/reporte_VehiculosSucursal.html',{'vehiculo':vehiculo})
 

class ReporteProveedoresUsados(View):

	
	def get(self, request, **kwargs):

		repuestos = Repuesto.objects.all()
 		
		proveedores =repuestos.values("proveedor").annotate(usados=Count('proveedor')).order_by(Coalesce('usados', 'usados').desc())
		for m in proveedores:
			m['proveedor'] = str(Proveedor.objects.get(id=m["proveedor"]).nombre)
		
		return render (request, 'reporte/reporte_Provedoores.html',{'proveedores':proveedores})


class ReporteSucursalRepuestos(View):

	
	def get(self, request, **kwargs):

		repuestosSucursal = SucursalRepuesto.objects.all()
 		
		cantidadRepuestos = repuestosSucursal.values("sucursal").annotate(cantidad=Sum('cantidad')).order_by(Coalesce('cantidad', 'cantidad').desc())
		for m in cantidadRepuestos:
			m['sucursal'] = str(Sucursal.objects.get(id=m["sucursal"]).nombre)

		print cantidadRepuestos
		return render (request, 'reporte/reporte_RepuestosSucursales.html',{'cantidadRepuestos':cantidadRepuestos})



