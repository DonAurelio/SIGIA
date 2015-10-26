# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Cotizacion
# Register your models here.

class AdminCotizacion(admin.ModelAdmin):
	#atributos
	
	list_display = ('id', 'empleado', 'cliente',
		 'vehiculo', 'fecha', 'fecha_vencimiento', 'forma_pago')
	#atributos por los que se buscara
	search_fields = ('id', 'cliente')
	  
#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Cotizacion, AdminCotizacion)
