# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Sucursal, SucursalRepuesto, SucursalVehiculo

class AdminSucursal(admin.ModelAdmin):

	list_display = ('id', 'nombre', 'direccion','telefono', 'ciudad','habilitado')

	search_fields = ('id','nombre')

admin.site.register(Sucursal,AdminSucursal)

class AdminSucursalRepuesto(admin.ModelAdmin):
	
	list_display = ('id','nombre_sucursal','nombre_repuesto','cantidad_repuesto')

	search_fields = ('nombre_sucursal','nombre_repuesto','cantidad_repuesto')
	
admin.site.register(SucursalRepuesto, AdminSucursalRepuesto)

class AdminSucursalVehiculo(admin.ModelAdmin):

	list_display = ('id','nombre_sucursal','numero_serie','color_vehiculo','cantidad_vehiculo')

	search_fields = ('nombre_sucursal','numero_serie','color_vehiculo','cantidad_vehiculo')

admin.site.register(SucursalVehiculo, AdminSucursalVehiculo)
