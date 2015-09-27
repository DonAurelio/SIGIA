from django.db import models

# Create your models here.
class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key=True)
	nombre = models.CharField(null=True,blank=True,max_length=50)
	apellido = models.CharField(null=True,blank=True,max_length=50)
	ciudad = models.CharField(null=True,blank=True,max_length=50)
	departamento = models.CharField(null=True,blank=True,max_length=50)
	telefono = models.CharField(null=True,blank=True,max_length=10)
	celular = models.CharField(null=True,blank=True,max_length=20)
	email = models.EmailField(null=True,blank=True,max_length=20)