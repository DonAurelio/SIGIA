# -*- encoding: utf-8 -*-

from django.db import models

class Proveedor(models.Model):
	nombre = models.CharField(max_length=50,null=True,blank=True)
	direccion = models.CharField(max_length=100,null=True,blank=True)
	telefono = models.CharField(max_length=10,null=True,blank=True)
	ciudad = models.CharField(max_length=20,null=True,blank=True)
	email = models.EmailField(max_length=50,null=True,blank=True)
	habilitado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre 

	def __unicode__(self):
		return self.nombre
		
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Proveedores"




