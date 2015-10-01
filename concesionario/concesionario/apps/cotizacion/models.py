from django.db import models
from concesionario.apps.empleado import Empleado
 
#ATRIBUTOS DE COTIZACION		
#id_cotizacion				
#empleado
#cliente
#vehiculo
#fecha
#fecha_vencimiento
#forma_Pago

#Define la organizacion del los datos de una cotizacion en la base de datos
class Cotizacion(models.Model):
#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"

	#Empleado que realiza la cotizacion, relacion uno a muchos 
	empleado= models.ForeignKey(Empleado)
 
	#Cliente que solicita la cotizacion, relacion uno a muchos 
	cliente= models.ForeignKey(Cliente)

	#Vehiculo cotizado, relacion uno a muchos 
	vehiculo= models.ForeignKey(Vehiculo)

	#Fecha en que se realiza la cotizacion
	fecha=models.DateField(blank=True, null=True)


	#Fecha de vencimiento de la cotizacion
	fecha_vencimiento=models.DateField(blank=True, null=True)

	#Formas de pago
	forma_Pago = models.CharField(null=True,blank=True,max_length=50)

#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['fecha']
		verbose_name_plural = "Cotizaciones"

	#Permite determinar una representacion en string del objeto repuesto
	def __str__(self):
		return self.fecha

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.fecha 






