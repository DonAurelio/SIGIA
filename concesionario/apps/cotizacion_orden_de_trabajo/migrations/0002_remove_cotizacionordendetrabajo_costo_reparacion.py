# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacionordendetrabajo',
            name='costo_reparacion',
        ),
    ]
