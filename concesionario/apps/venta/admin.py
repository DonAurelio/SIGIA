# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Venta

class AdminVenta(admin.ModelAdmin):
	list_display = ('id','empleado', 'cliente', 'vehiculo', 'fecha_venta',
		'descuento', 'precio_venta', 'forma_pago')
	search_fields = ('empleado', 'cliente', 'vehiculo')

admin.site.register(Venta, AdminVenta)