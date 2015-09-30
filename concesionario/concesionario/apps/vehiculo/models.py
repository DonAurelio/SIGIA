from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Vehiculo(models.Model):
	numero_serie = models.CharField(null=True, blank=True, max_length=100)
	marca = models.CharField(null=True, blank=True, max_length=100)
	precio = models.FloatField(null=True, blank=True)
	modelo = models.CharField(null=True, blank=True, max_length=100)
	potencia = models.CharField(null=True, blank=True, max_length=100)
	motor = models.CharField(null=True, blank=True, max_length=100)
	caracteristicas = models.TextField(null=True, blank=True)
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/vehiculos/")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})
	capacidad = models.CharField(null=True, blank=True, max_length=50)

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