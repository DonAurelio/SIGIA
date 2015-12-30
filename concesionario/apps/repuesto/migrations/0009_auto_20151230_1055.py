# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0008_auto_20151230_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='proveedor',
            field=models.OneToOneField(default=b'ACME', to='proveedor.Proveedor'),
        ),
    ]
