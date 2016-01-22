# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0002_auto_20160114_2107'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sucursalrepuesto',
            unique_together=set([('sucursal', 'repuesto')]),
        ),
    ]
