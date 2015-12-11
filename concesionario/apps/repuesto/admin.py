# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Repuesto, SucursalRepuesto

# Register your models here.
class AdminRepuesto(admin.ModelAdmin):
	#atributos
	list_display = (
		'id', 'nombre', 'precio',
		'marca', 'clasificacion',
		'imagen', 'proveedor', 'descripcion' )
	#atributos por los que se buscara
	search_fields = ('id', 'nombre')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Repuesto, AdminRepuesto)

# Register your models here.
class AdminSucursalRepuesto(admin.ModelAdmin):
	
	list_display = ('nombre_sucursal','nombre_repuesto','cantidad_repuesto')
	search_fields = ('nombre_sucursal','nombre_repuesto','cantidad_repuesto')
	
#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(SucursalRepuesto, AdminSucursalRepuesto)