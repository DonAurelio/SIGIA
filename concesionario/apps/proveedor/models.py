# -*- encoding: utf-8 -*-

from django.db import models

class Proveedor(models.Model):
	#Nombre del proveedor
	nombre = models.CharField(max_length=50)
	#Direccion donde se encuentra el alamcen del proveedor
	direccion = models.CharField(max_length=100)
	#Telefono del proveedor
	telefono = models.CharField(max_length=10)
	#Cuidad donde se encuentra el proveedor
	ciudad = models.CharField(max_length=20)
	#Correo electronico del proveedor
	email = models.EmailField(max_length=50)
	#Si el proveedor se encuentra activo para el sistema o no
	habilitado = models.BooleanField(default=True)

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Proveedores"

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre
