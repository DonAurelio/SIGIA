from django.db import models
from concesionario.apps.empleado.models import Empleado
from concesionario.apps.cliente.models import Cliente
from concesionario.apps.vehiculo.models import Vehiculo
from concesionario.apps.empleado.models import Empleado

 
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

	# Forma de pago en que se realiza la compra
	CREDITO = 'Credito'
	EFECTIVO = 'Efectivo'
	TARJETA_CREDITO = 'Tarjeta_credito'
	TARJETA_DEBITO = 'Tarjeta_debito'
	
	forma_pago_choices = (
		(CREDITO, 'Credito'),
		(EFECTIVO, 'Efectivo'),
		(TARJETA_CREDITO, 'Tarjeta de credito'),
		(TARJETA_DEBITO, 'Tarjeta de debito'),
	)

	forma_pago = models.CharField(max_length=20, choices=forma_pago_choices, default=EFECTIVO)

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






