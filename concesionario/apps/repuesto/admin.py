# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Repuesto

class AdminRepuesto(admin.ModelAdmin):

	list_display = (
		'id', 'nombre', 'precio',
		'marca', 'clasificacion',
		'imagen', 'proveedor', 'descripcion' )

	search_fields = ('id', 'nombre')

admin.site.register(Repuesto, AdminRepuesto)

