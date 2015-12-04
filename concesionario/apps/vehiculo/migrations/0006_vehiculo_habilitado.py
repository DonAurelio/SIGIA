# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_vehiculo_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
