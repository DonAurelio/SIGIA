from django.contrib import admin
from .models import FacturaOrdenDeTrabajo

class FacturaOrdenDeTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id','cotizacion','costo_total')
    search_fields = ('id',)

admin.site.register(FacturaOrdenDeTrabajo,FacturaOrdenDeTrabajoAdmin)
