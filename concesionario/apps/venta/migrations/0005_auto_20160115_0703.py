# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_auto_20160115_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='sucursal_vehiculo',
            field=models.ForeignKey(to='sucursal.SucursalVehiculo'),
        ),
    ]
