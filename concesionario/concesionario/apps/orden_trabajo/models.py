from django.db import models
from django.contrib.auth.models import User
from concesionario.apps.cliente import Cliente
from concesionario.apps.repuesto import Repuesto

# Create your models here.
class OrdenTrabajo(models.Model):
	empleado = models.OneToOneField(User)
	cliente = models.OneToOneField(Cliente)
	placa_vehiculo = models.CharField(max_length=7,null=True,blank=True)
	fecha_entrada = models.DateField(auto_now=True)
	fecha_salida = models.DateField()
	descripcion = models.TextField()
	estado = models.BooleanField()
	

class FacturaOrdenTrabajo(models.Model):
	id_factura_orden_trabajo = models.AutoField()
	orden_trabajo = models.OneToOneField(OrdenTrabajo)
	repuestos = models.ManyToManyField(Repuesto)
	costo_mano_obra = models.BigIntegerField()
	costo_repuestos = models.BigIntegerField()
	costo_total = models.BigIntegerField() 
