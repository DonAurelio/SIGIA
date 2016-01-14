# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from apps.sucursal.models import Sucursal
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
		
"""
Atributos de User
(username,first_name,last_name,email,password,groups,user_permissions,is_staff,is_active,
is_superuser,last_login,date_joined)

Metodos Utiles 
email_user(subject, message, from_email=None, **kwargs)
"""

VENDEDOR = 'Vendedor'
JEFE_TALLER = 'Jefe de taller'
GERENTE = 'Gerente'

tipo_choice = (
	(VENDEDOR, 'Vendedor'),
	(JEFE_TALLER, 'Jefe de taller'),
	(GERENTE, 'Gerente'),
 )

class Empleado(models.Model):
	"""Define la organizacion del los datos de un empleado en la base de datos."""
	
	#related_name permite hacer una referencia desde user a empleado de la siguiente forma user.empleado
	user = models.OneToOneField(User,related_name='empleado',null=True)
	#Indentificacion del empleado, debe ser unica
	identificacion = models.CharField(max_length=20,unique=True,null=False,blank=True)
	#Direccion de residencia del empleado
	direccion = models.CharField(null=False,blank=True,max_length=200)
	#telefono de residencia del empleado
	telefono = models.CharField(null=False,blank=True,max_length=10)
	#Salario actual del empleado
	salario =  models.BigIntegerField(null=False,blank=True)
	#Sucursal a la que pertenece el empleado 
	sucursal = models.ForeignKey(Sucursal,default=None)
	#Imagen o foto del empleado
	#Tipos de empleados que se puden crear
	tipo = models.CharField(null=False,max_length=20, choices=tipo_choice,default=VENDEDOR)
	#Estado de la empleado, Activa/inactiva
	habilitado = models.BooleanField(default = True)
	#Foto de perfil del empleado
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/empleado")
	#Thumbnail que permite reducir la imagen del empleado 
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})

	#Permite hacer modificaciones agregadas a la representacion del modelo 
	class Meta:
		ordering = ['identificacion']
		verbose_name_plural = "Empleados"

	#Permite determinar una representacion en string del objeto empleado
	def __str__(self):
		return self.user.first_name 

	#Permite determinar una represetacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.user.first_name
			