# -*- encoding: utf-8 -*-

from django.db import models
from apps.repuesto.models import Repuesto
from apps.orden_de_trabajo.models import OrdenDeTrabajo

#Define la organizacion de los datos de una factura de orden de trabajo en
#la base de datos 
class FacturaOrdenTrabajo(models.Model):
	#Orden de trabajo a la que pertenece la factura
	orden_trabajo = models.OneToOneField(OrdenDeTrabajo)
	#Repuestos usados para la reparacion de un vehiculo
	repuestos = models.ManyToManyField(Repuesto)
	#Costo de la mano de obra 
	costo_mano_obra = models.FloatField(null=True,blank=True)
	#Costo total de los repuesto usados en la reparacion del vehiculo
	costo_repuestos =  models.FloatField(null=True,blank=True)
	#Costo total de la reparacion 
	costo_total =  models.FloatField(null=True,blank=True)
