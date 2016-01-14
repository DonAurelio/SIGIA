# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0001_initial'),
        ('vehiculo', '0001_initial'),
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendetrabajo',
            name='sucursal',
            field=models.ForeignKey(default=None, to='sucursal.Sucursal'),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='vehiculo',
            field=models.ForeignKey(default=None, to='vehiculo.Vehiculo'),
        ),
    ]
