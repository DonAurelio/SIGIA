from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Vehiculo(models.Model):
	numero_serie = models.AutoField(primary_key=True)
	marca = models.CharField(max_length=50,null=True,blank=True)
	precio = models.BigIntegerField(null=True,blank=True)
	modelo = models.IntegerField(null=True,blank=True)
	potencia = models.IntegerField(null=True,blank=True)
	motor = models.CharField(max_length=50,null=True,blank=True)
	caracteristicas = models.TextField(null=True,blank=True)
	capacidad = models.IntegerField(null=True,blank=True)
	color = models.CharField(max_length=50,null=True,blank=True)
	cantidad  = models.IntegerField(null=True,blank=True)
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/vehiculos")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 100)],
									  format='JPEG',
									  options={'quality': 60})

	
	AUTOMOVIL = 'Automovil'
	CAMPERO = 'Campero'
	CAMIONETA = 'Camioneta'
	MICROBUS = 'Microbus'
	BUSETA = 'Buseta'
	BUS_METROPOLITANO = 'Bus Metropolitano'
	CAMION_MEDIANO_F350 = 'Camion mediano F-350'
	CAMION_GRADE_F600 = 'Camion Grade F-600' 
	CAMION_C3 = 'Camion C3'
	TRACTO_CAMION = 'Tracto Camion'
	CAMION_C4 = 'Camion C4'

	tipos = (
		(AUTOMOVIL,'AUTOMOVIL'),
		(CAMPERO,'CAMPERO'),
		(CAMIONETA,'CAMIONETA'),
		(MICROBUS,'MICROBUS'),
		(BUSETA,'BUSETA'),
		(BUS_METROPOLITANO,'BUS METROPOLITANO'),
		(CAMION_MEDIANO_F350,'CAMION MEDIANO F350'),
		(CAMION_GRADE_F600,'CAMION GRADE F600'),
		(CAMION_C3,'CAMION C3'),
		(TRACTO_CAMION,'TRACTO CAMION'),
		(CAMION_C4,'CAMION C4'),
		)

	tipo = models.CharField(null=True,blank=True,max_length=100,choices=tipos,default=AUTOMOVIL)
	