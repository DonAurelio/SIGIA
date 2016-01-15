# -*- encoding: utf-8 -*-

from django.db import models
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.repuesto.models import Repuesto

# Create your models here.

class CotizacionOrdenDeTrabajo(models.Model):
	#Orden de trabajo para la cual se relizara la cotizacion
	orden_de_trabajo = models.OneToOneField(OrdenDeTrabajo)
	#Repuestos involucrados en la cotizacion
	repuestos = models.ManyToManyField(Repuesto)
	#Detalles de la reparacion del vehiculo
	detalles = models.TextField()
	#Costo de la reparacion del vehiculo
	costo = models.FloatField()
	#Fecha hasta la cual es valida la cotizacion
	fecha_vencimiento = models.DateField()
	#Se inhabilita una cotizacion cuando el vehiculo ha sido reparado 
	#o el cliente retira el vehiculo sin haber sido reparado
	habilitado = models.BooleanField(default=True)

	class Meta:
		ordering = ['fecha_vencimiento']
		verbose_name_plural = "Cotizaciones Ordenes de Trabajo"

	def __str__(self):
		return "Cotizacion"

	def __unicode__(self):
		return u"Cotizacion"

