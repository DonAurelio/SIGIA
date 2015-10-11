from django.contrib import admin
from .models import FacturaOrdenTrabajo

#Permite administrar la visualizacion de los datos de la base de datos en el sitio de administracion
class AdminFacturaOrdenTrabajo(admin.ModelAdmin):
	#Se establece la informacion que se mostrara en el sitio de administracion
	list_display = ('id','orden_trabajo','costo_mano_obra','costo_repuestos','costo_total')
	
	#Se establece el parametro de busqueda
	search_fields = ('id',)

#Se registra el AdminFacturaOrdenTrabajo
admin.site.register(FacturaOrdenTrabajo,AdminFacturaOrdenTrabajo)