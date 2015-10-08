from django.views.generic.edit import CreateView 
from concesionario.apps.cotizacion.models import Cotizacion 
 
class CrearCotizacion(CreateView): 
	template_name = 'cotizacion/includes/crear.html'
	model = Cotizacion 
	fields = ['empleado', 'cliente', 'vehiculo', 'fecha','fecha_vencimiento', 'forma_pago'] 
