from django.db import models
from django.contrib.auth.models import User
from concesionario.apps.cliente.models import Cliente
from concesionario.apps.vehiculo.models import Vehiculo

# Create your models here.
class Cotizacion(models.Model):
	id_cotizacion = models.AutoField(primary_key=True)
	empleado = models.OneToOneField(User)
	cliente = models.OneToOneField(Cliente)
	vehiculo = models.OneToOneField(Vehiculo)
	fecha = models.DateField()
	fecha_vencimiento = models.DateField()

	EFECTIVO = 'Efectivo'
	TARJETA_CREDITO = 'Tarjeta_credito'
	TARJETA_DEBITO = 'Tarjeta_debito'

	tipo = (
		
		(EFECTIVO, 'Efectivo'),
		(TARJETA_CREDITO, 'Tarjeta de credito'),
		(TARJETA_DEBITO, 'Tarjeta de debito'),
	)

	forma_pago = models.CharField(max_length=20,choices=tipo,default=EFECTIVO)
