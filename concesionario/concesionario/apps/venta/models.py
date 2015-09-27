from django.db import models

# Create your models here.
class Venta(models.Model):
	id_venta = models.AutoField(primary_key=True)
	fecha_compra = models.DateTimeField(auto_now=True,null=True,blank=True)
	precio_venta = models.BigIntegerField(null=True,blank=True)
	descuento = models.FloatField(null=True,blank=True)
	EFECTIVO = 'Efectivo'
	TARJETA_CREDITO = 'Tarjeta_credito'
	TARJETA_DEBITO = 'Tarjeta_debito'

	tipo = (
		
		(EFECTIVO, 'Efectivo'),
		(TARJETA_CREDITO, 'Tarjeta de credito'),
		(TARJETA_DEBITO, 'Tarjeta de debito'),
	)

	forma_pago = models.CharField(max_length=20,choices=tipo,default=EFECTIVO)