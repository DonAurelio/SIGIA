# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20160114_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(default=None, to='empleado.Empleado', null=True),
        ),
    ]
