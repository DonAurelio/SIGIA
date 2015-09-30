from django.contrib import admin
from .models import Vehiculo

class Vehiculo_Admin(admin.ModelAdmin):
	list_display = ('numero_serie', 'marca', 'precio', 'modelo', 'potencia', 'motor',
		'caracteristicas', 'imagen', 'capacidad', 'tipo')
	search_fields = ('numero_serie', 'marca', 'modelo')

admin.site.register(Vehiculo, Vehiculo_Admin)
