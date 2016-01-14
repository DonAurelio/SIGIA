# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('empleado', '0001_initial'),
        ('cotizacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(to='empleado.Empleado'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='vehiculo',
            field=models.ForeignKey(to='vehiculo.Vehiculo'),
        ),
    ]
