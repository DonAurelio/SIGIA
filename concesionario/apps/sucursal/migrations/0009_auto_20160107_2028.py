# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0008_auto_20151231_1042'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sucursalvehiculo',
            unique_together=set([('sucursal', 'vehiculo', 'color')]),
        ),
    ]
