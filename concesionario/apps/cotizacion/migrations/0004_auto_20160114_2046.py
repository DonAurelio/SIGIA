# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0003_auto_20160114_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(default=None, to='cliente.Cliente', null=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='vehiculo',
            field=models.ForeignKey(default=None, to='vehiculo.Vehiculo', null=True),
        ),
    ]
