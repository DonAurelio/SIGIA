# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0010_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='empleado',
            field=models.ForeignKey(related_name='ventas', to='empleado.Empleado'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='sucursal_vehiculo',
            field=models.ForeignKey(related_name='ventas', default=None, blank=True, to='sucursal.SucursalVehiculo', null=True),
        ),
    ]
