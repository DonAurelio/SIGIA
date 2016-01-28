# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0002_remove_cotizacionordendetrabajo_costo_reparacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacionordendetrabajo',
            name='costo_reparacion',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
