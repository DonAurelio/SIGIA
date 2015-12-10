# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
        ('vehiculo', '0007_auto_20151208_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal_vehiculo',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='sucursal_vehiculo',
            name='vehiculo',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='sucursal',
            field=models.ForeignKey(default=1, to='sucursal.Sucursal'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Sucursal_Vehiculo',
        ),
    ]
