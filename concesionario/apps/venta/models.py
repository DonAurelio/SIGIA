# -*- encoding: utf-8 -*-

from django.db import models
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

class Venta(models.Model):
	"""Define como se organizaran las ventas en la base de datos."""
	
	#Llave foranea al empleado que realiza la venta
	empleado = models.ForeignKey(Empleado)
	#Cliente que realiza la compra
	cliente = models.ForeignKey(Cliente)
	#Vehiculo de la venta
	vehiculo = models.ForeignKey(Vehiculo)
	#Fecha en que se realiza la venta
	fecha_venta = models.DateField(auto_now_add=True)
	#Descuento aplicado a la venta
	descuento = models.FloatField()
	#Precio final de la venta, precio vehiculo - descuento
	precio_venta = models.FloatField()
	#Forma de pago para la compra del vehiculo	
	forma_pago = models.CharField(max_length=20, choices=forma_pago_choices, default=EFECTIVO)
	#Estado de la venta, Activa/inactiva
	habilitado = models.BooleanField(default = True)

	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['fecha_venta']
		verbose_name_plural = "Ventas"

	#Permite determinar una representacion en string del objeto empleado
	def __str__(self):
		return self.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.nombre