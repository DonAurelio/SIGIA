# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0009_empleado_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(to='sucursal.Sucursal'),
        ),
    ]
