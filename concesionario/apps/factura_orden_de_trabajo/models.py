from django.db import models
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo

class FacturaOrdenDeTrabajo(models.Model):
	# Cotizacion de la cual se hace la factura de la orden de trabajo
	# related_name para poder acceder desde la cotizacion orden de trabaja hacia la factura
	cotizacion = models.OneToOneField(CotizacionOrdenDeTrabajo,related_name='factura')
	# Costo de la reparacion + la suma del costo de los repuestos
	costo_total = models.FloatField(default=0)

	class Meta:
		verbose_name_plural = "Facturas de Ordenes de Trabajo"

	def save(self,*args,**kwargs):
		self.costo_total = self.cotizacion.costo_total()
		super(FacturaOrdenDeTrabajo,self).save(*args,**kwargs)
