# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
        ('vehiculo', '0001_initial'),
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='repuestos',
            field=models.ManyToManyField(to='repuesto.Repuesto'),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='vehiculos',
            field=models.ManyToManyField(to='vehiculo.Vehiculo'),
        ),
    ]
