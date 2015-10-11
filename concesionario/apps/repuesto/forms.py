# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView 
from .models import Repuesto
 
class CrearRepuesto(CreateView): 
	template_name = 'repuesto/includes/crear.html'
	model = Repuesto
	fields = ['nombre', 'precio', 'marca', 'clasificacion', 'cantidad',
	'imagen', 'provedor', 'descripcion']