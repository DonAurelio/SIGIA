# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView
from .models import Repuesto
 
class CrearRepuesto(CreateView): 
    model = Repuesto
    fields = ['nombre', 'precio', 'marca', 'clasificacion', 'cantidad',
    'imagen', 'proveedor', 'descripcion', 'sucursal']

class ActualizarRepuesto(UpdateView): 
    model = Repuesto 
    fields = ['nombre', 'precio', 'marca', 'clasificacion', 'cantidad',
    'imagen', 'proveedor', 'descripcion', 'sucursal']
    #template_name_suffix = '_update_form'