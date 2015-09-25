from django.db import models

# Create your models here.
class Cliente(models.models):
	id_cliente = models.AutoField(primary_key=True)
	nombre = models.ChartField(null=True,blank=True,max_lenght=50)
	apellido = models.ChartField(null=True,blank=True,max_lenght=50)
	ciudad = models.ChartField(null=True,blank=True,max_lenght=50)
	departamento = models.ChartField(null=True,blank=True,max_lenght=50)
	telefono = models.ChartField(null=True,blank=True,max_lenght=10)
	celular = models.ChartField(null=True,blank=True,max_lenght=20)
	email = models.EmailField(null=True,blank=True,max_lenght=20)