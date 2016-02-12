# -*- encoding: utf-8 -*-

from django.db import models
from apps.vehiculo.models import Vehiculo
from apps.repuesto.models import Repuesto

class Sucursal(models.Model):
	"""Define la organizacion de los datos de una sucursal en la base de datos"""

	#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"

	#Nombre de la sucursal
	nombre = models.CharField(null=True,blank=True,max_length=20,unique=True)
	#Direccion en la cual queda ubicada la sucursal
	direccion = models.CharField(null=True,blank=True,max_length=50)
	#Telefono de la sucursal
	telefono = models.CharField(null=True,blank=True,max_length=10)
	#Ciudad donde queda ubicada la sucursal
	ciudad = models.CharField(null=True,blank=True,max_length = 50)
	#Estado de la sucursa, Activa/inactiva
	habilitado = models.BooleanField(default = True)
	#Vehiculos que tiene la sucursal en venta
	#related_name para poder acceder desde una instancia vehiculo a su sucursal
	vehiculos = models.ManyToManyField(Vehiculo,through='SucursalVehiculo',related_name='sucursal')
	#Repuestos que tiene la sucursal
	#related_name para poder acceder desde una instancia repuesto a su sucursal
	repuestos = models.ManyToManyField(Repuesto,through='SucursalRepuesto',related_name='sucursal')

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


class SucursalVehiculo(models.Model):
	"""Define la cantidad que existe de cada vehiculo por sucursal."""

	#Sucursal a la que pertenece el vehiculo
	sucursal = models.ForeignKey(Sucursal,default=None)
	#Vehiculo
	vehiculo = models.ForeignKey(Vehiculo,default=None)
	#Color del vehiculo
	color = models.CharField(null=True,blank=True,max_length=20)
	#Cantidad disponible en stock del repuesto en la sucursal
	cantidad = models.IntegerField(null=True,blank=True)
	#Estado de la vehiculo, Activa/inactiva
	habilitado = models.BooleanField(default=True)

	class Meta:
		ordering = ['cantidad']
		verbose_name_plural = 'Vehiculos Sucursal'
		unique_together = ("sucursal", "vehiculo", "color")

	def __str__(self):
		return self.vehiculo.marca + " " + self.vehiculo.modelo + " " + self.color

	def __unicode__(self):
		return self.vehiculo.marca + " " + self.vehiculo.modelo + " " + self.color

	def nombre_sucursal(self):
		return self.sucursal.nombre

	def numero_serie(self):
		return self.vehiculo.numero_serie

	def color_vehiculo(self):
		return self.color

	def marca_vehiculo(self):
		return sefl.vehiculo.marca

	def cantidad_vehiculo(self):
		return self.cantidad


class SucursalRepuesto(models.Model):
	"""Define la cantidad que existe de cada repuesto por sucursal."""

	#Sucursal a la que pertenece el repuesto
	sucursal = models.ForeignKey(Sucursal,default=None)
	#Repuesto
	repuesto = models.ForeignKey(Repuesto,default=None)
	#Cantidad disponible en stock del repuesto en la sucursal
	cantidad = models.IntegerField(null=True,blank=True)
	#Estado de la repuesto, Activa/inactiva
	habilitado = models.BooleanField(default = True)

	def nombre_sucursal(self):
		return self.sucursal.nombre

	def nombre_repuesto(self):
		return self.repuesto.nombre

	def cantidad_repuesto(self):
		return self.cantidad

	class Meta:
		ordering = ['cantidad']
		verbose_name_plural = 'Repuestos Sucursal'
		unique_together = ("sucursal", "repuesto")

	#Permite determinar una representacion en string del objeto SucursalRepuesto
	def __str__(self):
		return self.sucursal.nombre + " " + self.repuesto.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.sucursal.nombre + " " + self.repuesto.nombre
