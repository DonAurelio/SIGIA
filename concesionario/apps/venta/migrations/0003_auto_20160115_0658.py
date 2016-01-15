# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0002_auto_20160114_2107'),
        ('venta', '0002_auto_20160115_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='vehiculo',
        ),
        migrations.AddField(
            model_name='venta',
            name='sucursal_vehiculo',
            field=models.ForeignKey(default=None, to='sucursal.SucursalVehiculo'),
        ),
    ]
