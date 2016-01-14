# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_auto_20160114_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(default=None, to='cliente.Cliente'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(default=None, to='empleado.Empleado'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='vehiculo',
            field=models.ForeignKey(default=None, to='vehiculo.Vehiculo'),
        ),
    ]
