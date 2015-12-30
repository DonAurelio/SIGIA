# -*- encoding: utf-8 -*-

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from apps.sucursal.models import Sucursal
from apps.proveedor.models import Proveedor

#Categorias de repuesto
AUTOMOTRIZ = 'Automotriz'
FERRETERIA= 'Ferreteria'
PINTURAS='Pinturas'
RODAMIENTOS='Rodamientos'
SOLVENTES='Solventes'
BANDAS_CADENAS='Bandas_cadenas'
LIMPIEZA='Limpieza'
AUTOPARTES='Autopartes'
SELLOS_EMPAQUES='Sellos_empaques'
LUBRICANTES='Lubricantes'

tipo_choice = (
	(AUTOMOTRIZ, 'Automotriz'),
	(FERRETERIA, 'Ferreteria'),
	(PINTURAS, 'Pinturas'),
	(RODAMIENTOS, 'Rodamientos'),
	(SOLVENTES, 'Solventes'),
	(BANDAS_CADENAS, 'Bandas y cadenas'),
	(LIMPIEZA, 'Limpieza'),
	(AUTOPARTES, 'Autopartes'),
	(SELLOS_EMPAQUES, 'Sellos y empaques'),
	(LUBRICANTES, 'Lubricantes'),
 )

class Repuesto(models.Model):
	"""Define la organizacion del los datos de un repuesto en la base de datos."""
	
	#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"
	#Relacion del repuesto con sucursal
	sucursal_repuestos = models.ManyToManyField(Sucursal,through='SucursalRepuesto')
	#Nombre del repuesto
	nombre = models.CharField(null=True,blank=True,max_length=50)
	#Precio del repuesto
	precio = models.FloatField(null=True,blank=True)
	#Marca del repuesto
	marca = models.CharField(null=True,blank=True,max_length=20) 
	#Clasificacion del repuesto
	clasificacion = models.CharField(null=True,blank=True, max_length=20, choices=tipo_choice,default=SELLOS_EMPAQUES)
	#Imagen del repuesto
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/repuestos/")
	#Thumbnail que permite reducir la imagen del repuesto 
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})

	#Provedor del repuesto
	proveedor = models.OneToOneField(Proveedor, default=None)
	#Descripcion del repuesto
	descripcion = models.CharField(null=True,blank=True,max_length=100)
	
	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Repuestos"

	#Permite determinar una representacion en string del objeto repuesto
	def __str__(self):
		return self.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.nombre 

class SucursalRepuesto(models.Model):
	"""Define la cantidad que existe de cada repuesto por sucursal."""
	
	#Sucursal a la que pertenece el repuesto
	sucursal = models.ForeignKey(Sucursal)
	#Repuesto
	repuesto = models.ForeignKey(Repuesto)
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

	#Permite determinar una representacion en string del objeto SucursalRepuesto
	def __str__(self):
		return self.sucursal.nombre + " " + self.repuesto.nombre 

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.sucursal.nombre + " " + self.repuesto.nombre 
	

