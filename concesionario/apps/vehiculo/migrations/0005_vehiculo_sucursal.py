# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0003_auto_20151204_0409'),
        ('vehiculo', '0004_auto_20151008_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='sucursal',
            field=models.ManyToManyField(to='sucursal.Sucursal'),
        ),
    ]
