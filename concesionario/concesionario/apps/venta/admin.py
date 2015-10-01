from django.contrib import admin
from .models import Venta

class Venta_Admin(admin.ModelAdmin):
	list_display = ('empleado', 'cliente', 'vehiculo', 'fecha_venta',
		'descuento', 'precio_venta', 'forma_pago')
	search_fields = ('empleado', 'cliente', 'vehiculo')

admin.site.register(Venta, Venta_Admin)