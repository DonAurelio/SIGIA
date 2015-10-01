from django.db import models
from concesionario.apps.repuesto import Repuesto
#from concesionario.apps.orden_trabajo import OrdenTrabajo

#Define la organizacion de los datos de una factura de orden de trabajo en
#la base de datos 
class FacturaOrdenTrabajo(models.Model):
	#orden_trabajo = = models.OneToOneField(OrdenTrabajo)
	#Repuestos usados para la reparacion de un vehiculo
	repuestos = models.ManyToManyField(Repuesto)
	#Costo de la mano de obra 
	costo_mano_obra = models.FloatField(null=True,blank=True)
	#Costo total de los repuesto usados en la reparacion del vehiculo
	costo_repuestos =  models.FloatField(null=True,blank=True)
	#Costo total de la reparacion 
	costo_total =  models.FloatField(null=True,blank=True)
