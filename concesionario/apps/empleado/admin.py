from django.contrib import admin
from .models import Empleado
# Register your models here.

#Permite administrar la visualizacion de los datos de la base de datos en el sitio de administarcion
class AdminEmpleado(admin.ModelAdmin):
	#Se establece la informacion que se mostrara en el sitio de administarcion 
	list_display = ('user', 'identificacion', 'direccion','telefono', 'salario','imagen','thumbnail','tipo')
	#Se establece el parametro de busqueda
	search_fields = ('identificacion',)

#se registra el AdminEmpleado 
admin.site.register(Empleado,AdminEmpleado)