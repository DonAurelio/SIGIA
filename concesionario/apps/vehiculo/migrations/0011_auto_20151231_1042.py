# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0010_auto_20151230_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursalvehiculo',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='sucursalvehiculo',
            name='vehiculo',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='sucursal_vehiculos',
        ),
        migrations.DeleteModel(
            name='SucursalVehiculo',
        ),
    ]
