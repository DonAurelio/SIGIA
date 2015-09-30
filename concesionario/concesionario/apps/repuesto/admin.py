from django.contrib import admin
from concesionario.apps.repuesto.models import Repuesto
# Register your models here.
class AdminRepuesto(admin.ModelAdmin):
	#atributos
	list_display = ('id', 'nombre', 'precio',
		 'marca', 'clasificacion', 'cantidad', 'imagen', 'provedor', 'descripcion' )
	#atributos por los que se buscara
	search_fields = ('id', 'nombre')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Repuesto, AdminRepuesto)