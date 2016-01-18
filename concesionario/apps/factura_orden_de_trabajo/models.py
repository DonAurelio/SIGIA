from django.db import models
from apps.cotizacion_orden_de_trabajo.models import CotizacionOrdenDeTrabajo

class FacturaOrdenDeTrabajo(models.Model):
    # Cotizacion de la cual se hace la factura de la orden de trabajo
    cotizacion = models.OneToOneField(CotizacionOrdenDeTrabajo)
    # Costo de la reparacion + la suma del costo de los repuestos
    costo_total = models.FloatField()

    class Meta:
        verbose_name_plural = "Facturas de Ordenes de Trabajo"
