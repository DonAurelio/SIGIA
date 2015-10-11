# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Cliente

class Cliente_Admin(admin.ModelAdmin):
	list_display = ('identificacion', 'nombre', 'apellido',	'ciudad', 'departamento',
		'telefono','celular', 'celular', 'email')
	search_fields = ('identificacion', 'apellido', 'nombre')

admin.site.register(Cliente, Cliente_Admin)