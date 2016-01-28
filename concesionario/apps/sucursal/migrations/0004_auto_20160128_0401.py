# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0003_auto_20160122_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='repuestos',
            field=models.ManyToManyField(related_name='sucursal', through='sucursal.SucursalRepuesto', to='repuesto.Repuesto'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='vehiculos',
            field=models.ManyToManyField(related_name='sucursal', through='sucursal.SucursalVehiculo', to='vehiculo.Vehiculo'),
        ),
    ]
