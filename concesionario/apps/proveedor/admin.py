from django.contrib import admin
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
	list_display = (
		'id','nombre','direccion','telefono',
		'ciudad','email','habilitado')
	list_search = ('nombre',)

admin.site.register(Proveedor,ProveedorAdmin)
