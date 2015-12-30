# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0009_auto_20151230_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='proveedor',
            field=models.OneToOneField(default=None, to='proveedor.Proveedor'),
        ),
    ]
