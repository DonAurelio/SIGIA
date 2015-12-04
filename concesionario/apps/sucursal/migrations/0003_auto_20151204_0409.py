# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0002_auto_20150930_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='repuestos',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='vehiculos',
        ),
    ]
