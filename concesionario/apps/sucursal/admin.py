from django.contrib import admin
from .models import Sucursal


#Permite administrar la visualizacion de los datos de la base de datos en el sitio de administarcion
class AdminSucursal(admin.ModelAdmin):
	#Se establece la informacion que se mostrara en el sitio de administarcion 
	list_display = ('id', 'nombre', 'direccion','telefono', 'ciudad','activo')
	#Se establece el parametro de busqueda
	search_fields = ('id','nombre')

#se registra el AdminSucursal 
admin.site.register(Sucursal,AdminSucursal)
