from django.db import models
from concesionario.apps.vehiculo.models import Vehiculo
from concesionario.apps.repuesto.models import Repuesto

# Create your models here.
class Sucursal(models.Model):
	id_sucursal = models.AutoField(primary_key=True)
	nombre = models.CharField(null=True,blank=True,max_length=20)
	direccion = models.CharField(null=True,blank=True,max_length=50)
	telefono = models.CharField(null=True,blank=True,max_length=10)
	ciudad = models.CharField(null=True,blank=True,max_length = 50)
	activo = models.BooleanField(default = True)
	vehiculos = models.ManyToManyField(Vehiculo)
	repuestos = models.ManyToManyField(Repuesto)