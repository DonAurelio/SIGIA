from django.views.generic.edit import CreateView
from .models import Cliente

# Crea el registro de un cliente mediante la clase generica CreateView
class CrearCliente(CreateView):
	template_name = 'cliente/includes/crear.html'
	model = Cliente
	fields = ['identificacion', 'nombre', 'apellido', 'ciudad',
	'departamento', 'telefono', 'celular', 'email']