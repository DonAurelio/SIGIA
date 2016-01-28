# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import OrdenDeTrabajo
# Register your models here.

class AdminOrdenDeTrabajo(admin.ModelAdmin):
	#atributos
	list_display = ('id', 'empleado', 'cliente','sucursal','vehiculo',
		 'placa', 'fecha_entrada', 'fecha_salida','estado_reparacion',
		 'observacion','habilitado')
	#atributos por los que se buscara
	search_fields = ('id', 'placa')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(OrdenDeTrabajo, AdminOrdenDeTrabajo)
