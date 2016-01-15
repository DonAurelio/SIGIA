# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Venta

class AdminVenta(admin.ModelAdmin):
	list_display = ('id','empleado', 'cliente', 'sucursal_vehiculo', 'fecha_venta',
		'precio_venta', 'forma_pago')
	search_fields = ('empleado', 'cliente', 'sucursal_vehiculo')

admin.site.register(Venta, AdminVenta)