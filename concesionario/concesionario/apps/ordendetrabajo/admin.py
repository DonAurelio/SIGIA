from django.contrib import admin
from concesionario.apps.ordendetrabajo.models import Ordendetrabajo
# Register your models here.

class AdminOrdendetrabajo (admin.ModelAdmin):
	#atributos
	list_display = ('id', 'empleado', 'cliente',
		 'placa', 'fecha_entrada', 'fecha_salida', 'descripcion','estado_reparacion')
	#atributos por los que se buscara
	search_fields = ('id', 'placa')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Ordendetrabajo, AdminOrdendetrabajo)