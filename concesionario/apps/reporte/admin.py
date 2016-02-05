from django.contrib import admin
from .models import Reporte

class ReporteAdmin(admin.ModelAdmin):
	list_display = (
		'fecha','sucursal')
	list_search = ('fecha','sucursal')

#admin.site.register(Reporte,ReporteAdmin)