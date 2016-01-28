# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0004_auto_20160124_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotizacionordendetrabajo',
            old_name='costo',
            new_name='costo_reparacion',
        ),
        migrations.AlterField(
            model_name='repuestocantidad',
            name='cotizacion_orden_de_trabajo',
            field=models.ForeignKey(related_name='repuestos_cantidad', to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo'),
        ),
    ]
