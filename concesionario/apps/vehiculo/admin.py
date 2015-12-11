# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Vehiculo, SucursalVehiculo

class Vehiculo_Admin(admin.ModelAdmin):
	list_display = (
		'numero_serie', 'marca', 'precio', 'modelo', 'potencia', 'motor',
		'caracteristicas', 'imagen', 'capacidad', 'tipo')
	search_fields = ('vehiculo', 'unidades', 'color')

admin.site.register(Vehiculo, Vehiculo_Admin)

# Register your models here.
class AdminSucursalVehiculo(admin.ModelAdmin):
	list_display = ('nombre_sucursal','numero_serie','color_vehiculo','cantidad_vehiculo')
	search_fields = ('nombre_sucursal','numero_serie','color_vehiculo','cantidad_vehiculo')

# Register your models here.
admin.site.register(SucursalVehiculo, AdminSucursalVehiculo)

