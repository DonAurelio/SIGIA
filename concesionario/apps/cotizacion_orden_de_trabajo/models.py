# -*- encoding: utf-8 -*-

from django.db import models
from apps.orden_de_trabajo.models import OrdenDeTrabajo
from apps.repuesto.models import Repuesto
from datetime import datetime


class CotizacionOrdenDeTrabajo(models.Model):
	#Orden de trabajo para la cual se relizara la cotizacion
	#related_name para poder acceder desde orden de trabajo a CotizacionOrdenDeTrabajo
	orden_de_trabajo = models.OneToOneField(OrdenDeTrabajo,related_name='cotizacion')
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
		return "Cotizacion {}".format(self.id)

	def __unicode__(self):
		return u"Cotizacion {}".format(self.id)

	def es_valida(self):
		""" Documentacion es_valida

			Determina se la cotizacion es valida o no se ha vencido
			hasta la fecha actual.
		"""
		if datetime.now().date() > self.fecha_vencimiento:
			return False
		return True


class RepuestoCantidad(models.Model):
	# identificacion de la Cotizacion orden de trabajo
	# related_name para poder acceder desde una instancia de CotizacionOrdenDeTrabajo a RepuestoCantidad
	cotizacion_orden_de_trabajo = models.ForeignKey(CotizacionOrdenDeTrabajo, related_name='repuestos')
	# Repuesto a usar
	repuesto = models.ForeignKey(Repuesto)
	# Cantidad del repuesto a usar en la reparación
	cantidad = models.IntegerField()

	class Meta:
		verbose_name_plural = "Repuestos Cantidad"
		unique_together = (("cotizacion_orden_de_trabajo", "repuesto"),)
