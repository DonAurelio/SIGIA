from django.db import models
from concesionario.apps.models import Vehiculo
from concesionario.apps.models import Repuesto

# Create your models here.
class Sucursal(models.models):
	id_sucursal = models.AutoField(primary_key=True)
	nombre = models.ChartField(null = True, blank = True, max_lenght = 20)
	direccion = models.ChartField(null = True, blank = True, max_lenght = 50)
	telefono = models.ChartField(null = True, blank = True, max_lenght = 10)
	ciudad = models.ChartField(null = True, blank = True, max_lenght = 50)
	activo = models.BooleanField(null = True, blank = True, default = True)
	vehiculos = models.ManyToManyField(Vehiculo)
	repuestos = models.ManyToManyField(Repuesto)