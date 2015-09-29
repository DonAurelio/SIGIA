from django.db import models
from concesionario.apps.vehiculo.models import Vehiculo
from concesionario.apps.repuesto.models import Repuesto

#Define la organizacion de los datos de una sucursal en la base de datos
class Sucursal(models.Model):
	#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"
	#Nombre de la sucursal
	nombre = models.CharField(null=True,blank=True,max_length=20)
	#Direccion en la cual queda ubicada la sucursal
	direccion = models.CharField(null=True,blank=True,max_length=50)
	#Telefono de la sucursal
	telefono = models.CharField(null=True,blank=True,max_length=10)
	#Ciudad donde queda ubicada la sucursal
	ciudad = models.CharField(null=True,blank=True,max_length = 50)
	#Estado de la sucursa, Activa/inactiva
	activo = models.BooleanField(default = True)
	#Vehiculos que se venden en dicha sucursal
	vehiculos = models.ManyToManyField(Vehiculo)
	#Repuestos que se venden y se usan en dicha sucursal
	repuestos = models.ManyToManyField(Repuesto)

	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Sucursales"

	#Permite determinar una representacion en string del objeto empleado
	def __str__(self):
		return self.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.nombre