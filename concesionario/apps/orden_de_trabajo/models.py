# -*- encoding: utf-8 -*-

from django.db import models
from .validators import validador_placa
from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.sucursal.models import Sucursal
from apps.vehiculo.models import Vehiculo


#Estados de la reparacion del vehiculo

#El vehiculo esta en el taller, pero no se ha revisado
PENDIENTE = 'Pendiente'
#Ya esta la cotización de los daños del vehiculo
COTIZADO = 'Cotizado'
#El vehiculo esta reparado
REPARADO = 'Reparado'
#El vehiuclo fue reparado y entregado al cliente
REPARADO_Y_ENTREGADO = 'Reparado y entregado'
#El vehiculo fue retirado ya que el cliente no acepto su reparacion
RETIRADO = 'Retirado'

tipo_choice = (
	(PENDIENTE, 'Pendiente'),
	(COTIZADO, 'Cotizado'),
	(REPARADO, 'Reparado'),
	(REPARADO_Y_ENTREGADO, 'Reparado y entregado'),
	(RETIRADO, 'Retirado'),
 )

class OrdenDeTrabajo(models.Model):
	"""Define la organizacion del los datos de una orden de trabajo en la base de datos."""

	#Empleado que realiza la orden de trabajo, relacion uno a muchos
	empleado = models.ForeignKey(Empleado,default=None)
	#Sucursal a la que ingresa el vehiculo
	sucursal = models.ForeignKey(Sucursal,default=None)
	#dueno del auto que entra al taller, relacion uno a muchos
	cliente = models.ForeignKey(Cliente,default=None)
	#vehiculo que va a ser reparado
	vehiculo = models.ForeignKey(Vehiculo,default=None)
	#placa del vehiculo que entra al taller
	placa = models.CharField(validators=[validador_placa],null=True,blank=True,max_length=7)
	#Fecha de entrada al taller
	fecha_entrada = models.DateField(auto_now_add=True,blank=True, null=True)
	#Fecha de salida del taller
	fecha_salida = models.DateField(blank=True, null=True)
	#Estado del vehiculo en el taller
	estado_reparacion = models.TextField(null=True,blank=True,max_length=50,choices=tipo_choice,default=PENDIENTE)
	#Observacion de los daños del vehiculo
	observacion = models.TextField(null=True,blank=True,max_length=200)
	#Estado de la OrdenDeTrabajo, Activa/inactiva
	habilitado = models.BooleanField(default = True)

	#Permite hacer modificaciones agregadas a la representacion del modelo
	class Meta:
		ordering = ['fecha_entrada']
		verbose_name_plural = "Orden de Trabajo"
		unique_together = ('placa','fecha_salida')

	#Permite determinar una representacion en string del objeto repuesto
	def __str__(self):
		return self.vehiculo.marca

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.vehiculo.marca
