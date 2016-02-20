# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import CotizacionOrdenDeTrabajo
from .models import RepuestoCantidad

class CotizacionOrdenDeTrabajoAdmin(admin.ModelAdmin):
	list_display = (
		'id','orden_de_trabajo',
		'costo_reparacion','fecha_vencimiento','habilitado')
	search_fields = ('id',)

admin.site.register(CotizacionOrdenDeTrabajo,CotizacionOrdenDeTrabajoAdmin)

class RepuestoCantidadAdmin(admin.ModelAdmin):
	list_display = ('id','cotizacion_orden_de_trabajo','repuesto','cantidad' )
	search_fields = ('id','cotizacion_orden_de_trabajo')

admin.site.register(RepuestoCantidad,RepuestoCantidadAdmin)
