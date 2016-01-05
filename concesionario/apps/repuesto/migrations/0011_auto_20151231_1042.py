# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0010_auto_20151230_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursalrepuesto',
            name='repuesto',
        ),
        migrations.RemoveField(
            model_name='sucursalrepuesto',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='sucursal_repuestos',
        ),
        migrations.DeleteModel(
            name='SucursalRepuesto',
        ),
    ]
