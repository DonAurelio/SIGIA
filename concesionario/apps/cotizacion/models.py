# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime    
from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.vehiculo.models import Vehiculo


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

#
class Cotizacion(models.Model):
	"""Define la organizacion del los datos de una cotizacion en la base de datos."""
	
	#Empleado que realiza la cotizacion, relacion uno a muchos 
	empleado= models.ForeignKey(Empleado,default=None)
	#Cliente que solicita la cotizacion, relacion uno a muchos 
	cliente= models.ForeignKey(Cliente,default=None)
	#Vehiculo cotizado, relacion uno a muchos 
	vehiculo= models.ForeignKey(Vehiculo,default=None)
	#Fecha en que se realiza la cotizacion
	fecha=models.DateField(auto_now_add=True,blank=True,null=True)
	#Fecha de vencimiento de la cotizacion
	fecha_vencimiento=models.DateField(blank=True,null=True)
	#Forma de pago en la que se realiza la cotizacion
	forma_pago = models.CharField(max_length=20,choices=forma_pago_choices, default=EFECTIVO)
	#Estado de la cotizacion, Activa/inactiva
	habilitado = models.BooleanField(default = True)
	
	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['fecha']
		verbose_name_plural = "Cotizaciones"

	#Permite determinar una representacion en string del objeto  
	def __str__(self):
		return self.fecha

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.fecha 
 



 
