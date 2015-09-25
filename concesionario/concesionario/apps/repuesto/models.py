from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Repuesto(models.Model):
	id_repuesto = models.AutoField(primary_key=True)
	nombre = models.ChartField(null=True,blank=True)
	precio = models.ChartField(null=True,blank=True)
	marca = models.ChartField(null=True,blank=True)
	proveedor = models.ChartField(null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	cantidad = models.IntegerField()
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/repuestos")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 100)],
									  format='JPEG',
									  options={'quality': 60}))

	AUTOMOTRIZ = 'Automotriz'
	FERRETERIA = 'Ferreteria'
	PINTURAS = 'Pinturas'
	RODAMIENTOS = 'Rodamientos'
	SOLVENTES = 'Solventes'
	BANDAS_CADENAS = 'Bandas y Cadenas'
	LIMPIEZA = 'Limpieza'
	AUTOPARTES = 'Autopartes'
	SELLOS_EMPAQUES = 'sellos y empaques'

	tipo = (

			(AUTOMOTRIZ,AUTOMOTRIZ),
			(FERRETERIA,FERRETERIA),
			(PINTURAS,PINTURAS),
			(RODAMIENTOS,RODAMIENTOS),
			(SOLVENTES,SOLVENTES),
			(BANDAS_CADENAS,BANDAS_CADENAS),
			(LIMPIEZA,LIMPIEZA),
			(AUTOPARTES,AUTOPARTES),
			(SELLOS_EMPAQUES),
			
		)


	clasificacion = models.ChartField(null=True,blank=True,choices=tipo,default=AUTOMOTRIZ)
	

	