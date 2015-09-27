from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Repuesto(models.Model):
	id_repuesto = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100,null=True,blank=True)
	precio = models.BigIntegerField()
	marca = models.CharField(max_length=100,null=True,blank=True)
	proveedor = models.CharField(max_length=100,null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	cantidad = models.IntegerField()
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/repuestos")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 100)],
									  format='JPEG',
									  options={'quality': 60})

	AUTOMOTRIZ = 'Automotriz'
	FERRETERIA = 'Ferreteria'
	PINTURAS = 'Pinturas'
	RODAMIENTOS = 'Rodamientos'
	SOLVENTES = 'Solventes'
	BANDAS_CADENAS = 'Bandas y Cadenas'
	LIMPIEZA = 'Limpieza'
	AUTOPARTES = 'Autopartes'
	SELLOS_EMPAQUES = 'Sellos y Empaques'

	tipo = (

			(AUTOMOTRIZ,'Automotriz'),
			(FERRETERIA,'Ferreteria'),
			(PINTURAS,'Pinturas'),
			(RODAMIENTOS,'Rodamientos'),
			(SOLVENTES,'Solventes'),
			(BANDAS_CADENAS,'Bandas y Cadenas'),
			(LIMPIEZA,'Limpieza'),
			(AUTOPARTES,'Autopartes'),
			(SELLOS_EMPAQUES,'Sellos y Empaques'),
			
		)


	clasificacion = models.CharField(max_length=100,null=True,blank=True,choices=tipo,default=AUTOMOTRIZ)
	

	