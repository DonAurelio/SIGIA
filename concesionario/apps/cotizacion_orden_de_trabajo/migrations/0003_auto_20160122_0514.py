# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0002_auto_20160119_0345'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='repuestocantidad',
            unique_together=set([('cotizacion_orden_de_trabajo', 'repuesto')]),
        ),
    ]
