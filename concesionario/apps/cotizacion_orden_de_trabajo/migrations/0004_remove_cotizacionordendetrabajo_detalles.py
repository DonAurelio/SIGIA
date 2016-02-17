# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0003_cotizacionordendetrabajo_costo_reparacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacionordendetrabajo',
            name='detalles',
        ),
    ]
