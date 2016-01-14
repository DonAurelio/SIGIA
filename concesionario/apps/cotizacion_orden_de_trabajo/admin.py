# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import CotizacionOrdenDeTrabajo

class CotizacionOrdenDeTrabajoAdmin(admin.ModelAdmin):
	list_display = (
		'id','orden_de_trabajo','detalles',
		'costo','fecha_vencimiento','habilitado')
	search_fields = ('id',) 

admin.site.register(CotizacionOrdenDeTrabajo,CotizacionOrdenDeTrabajoAdmin)
