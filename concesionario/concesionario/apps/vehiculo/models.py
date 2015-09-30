from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Vehiculo(models.Model):
	# Numero de serie que identifica al vehiculo
	numero_serie = models.CharField(null=True, blank=True, max_length=100)
	# Marca del vehiculo
	marca = models.CharField(null=True, blank=True, max_length=100)
	# Precio del vehiculo
	precio = models.FloatField(null=True, blank=True)
	# Modelo de fabricacion
	modelo = models.CharField(null=True, blank=True, max_length=100)
	# Potencia entregada por el motor
	potencia = models.CharField(null=True, blank=True, max_length=100)
	# nombre del motor
	motor = models.CharField(null=True, blank=True, max_length=200)
	# Caracteristicas adicionales del vehiculo
	caracteristicas = models.TextField(null=True, blank=True)
	# Imagen representativa del vehiculo
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/vehiculos/")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})
	# Capacidad expresada en carga o pasajeros
	capacidad = models.CharField(null=True, blank=True, max_length=50)

	#-- Creacion del Choices para 'tipo' de vehiculo
	AUTOMOVIL = 'Automovil'
	CAMPERO = 'Campero'
	CAMIONETA = 'Camioneta'
	MICROBUS = 'Microbus'
	BUSETA = 'Buseta'
	BUS = 'Bus'
	CAMION = 'Camion'
	TRACTO_CAMION = 'Tracto camion'
	TIPO_CHOICES = (
		(AUTOMOVIL, 'Automovil'),
		(CAMPERO, 'Campero'),
		(CAMIONETA, 'Camioneta'),
		(MICROBUS, 'Microbus'),
		(BUSETA, 'Buseta'),
		(BUS, 'Bus'),
		(CAMION, 'Camion'),
		(TRACTO_CAMION, 'Tracto camion'),
	)
	tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default=AUTOMOVIL)
	
	#-- Creacion del Choices para 'color' de vehiculo
	NEGRO = 'Negro'
	BLANCO = 'Blanco'
	BEIGE = 'Beige'
	GRIS = 'Gris'
	AZUL = 'Azul'
	AMARILLO = 'Amarillo'
	ROJO = 'Rojo'
	VERDE = 'Verde'
	COLOR_CHOICES = (
		(AUTOMOVIL, 'Automovil'),
		(NEGRO, 'Negro'),
		(BLANCO, 'Blanco'),
		(BEIGE, 'Beige'),
		(GRIS, 'Gris'),
		(AZUL, 'Azul'),
		(AMARILLO, 'Amarillo'),
		(ROJO, 'Rojo'),
		(VERDE, 'Verde'),
	)
	color = models.CharField(max_length=2, choices=COLOR_CHOICES, default=BEIGE)

	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['numero_serie']
		verbose_name_plural = "Vehiculos"

	#Permite determinar una representacion en string del objeto empleado
	def __str__(self):
		return self.user.numero_serie

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.user.numero_serie
			