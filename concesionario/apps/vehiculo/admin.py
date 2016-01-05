# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Vehiculo

class Vehiculo_Admin(admin.ModelAdmin):

	list_display = (
		'numero_serie', 'marca', 'precio', 'modelo', 'potencia', 'motor',
		'caracteristicas', 'imagen', 'capacidad', 'tipo')

	search_fields = ('vehiculo', 'unidades', 'color')

admin.site.register(Vehiculo, Vehiculo_Admin)