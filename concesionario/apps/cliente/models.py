# -*- encoding: utf-8 -*-

from django.db import models

# Modelo que representa los clientes de la sucursal
class Cliente(models.Model):
	"""Representacion del cliente en la base de datos."""

	# Numero documento identificacion del cliente
	identificacion = models.CharField(null=True, blank=True, max_length=100)
	# Nombre(s) del cliente
	nombre = models.CharField(null=True, blank=True, max_length=100)
	# Apellido(s) del cliente
	apellido = models.CharField(null=True, blank=True, max_length=100)
	# Ciudad de residencia del cliente
	ciudad = models.CharField(null=True, blank=True, max_length=100)
	# Departamento de residencia del cliente
	departamento = models.CharField(null=True, blank=True, max_length=100)
	# Telefono fijo
	telefono = models.CharField(null=True, blank=True, max_length=100)
	# Numero de celular del cliente
	celular = models.CharField(null=True, blank=True, max_length=100)
	# Correo electronico
	email = models.EmailField(null=True, blank=True, max_length=100)
	#Estado de la cliente, Activa/inactiva
	habilitado = models.BooleanField(default = True)

	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['apellido']
		verbose_name_plural = "Clientes"

	#Permite determinar una representacion en string del objeto empleado
	def __str__(self):
		return self.identificacion + " " + self.nombre

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.identificacion + " " + self.apellido + " " + self.nombre