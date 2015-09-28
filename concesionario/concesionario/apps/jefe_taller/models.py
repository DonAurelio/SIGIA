from django.db import models
from django.contrib.auth.models import User
from concesionario.apps.sucursal.models import Sucursal
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

#ATRIBUTOS DE USER 		#METODOS UTILES	
#username				#email_user(subject, message, from_email=None, **kwargs)
#first_name
#last_name
#email
#password
#groups
#user_permissions	
#is_staff
#is_active
#is_superuser
#last_login
#date_joined

class JefeTaller(models.Model):
	user = models.OneToOneField(User)
	identificacion = models.CharField(max_length=20,null=True,blank=True)
	direccion = models.CharField(null=True,blank=True,max_length=200)
	telefono = models.CharField(null=True,blank=True,max_length=10)
	salario =  models.BigIntegerField(null=True,blank=True)
	sucursal = models.OneToOneField(Sucursal,default=None)
	imagen = models.ImageField(null=True,blank=True,upload_to = "imagenes/cuenta/jefe_taller")
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})

