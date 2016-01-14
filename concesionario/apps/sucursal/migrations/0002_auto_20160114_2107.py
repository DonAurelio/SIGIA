# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursalrepuesto',
            name='repuesto',
            field=models.ForeignKey(default=None, to='repuesto.Repuesto'),
        ),
        migrations.AlterField(
            model_name='sucursalrepuesto',
            name='sucursal',
            field=models.ForeignKey(default=None, to='sucursal.Sucursal'),
        ),
        migrations.AlterField(
            model_name='sucursalvehiculo',
            name='sucursal',
            field=models.ForeignKey(default=None, to='sucursal.Sucursal'),
        ),
        migrations.AlterField(
            model_name='sucursalvehiculo',
            name='vehiculo',
            field=models.ForeignKey(default=None, to='vehiculo.Vehiculo'),
        ),
    ]
