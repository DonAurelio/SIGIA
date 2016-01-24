# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0003_auto_20160122_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacionordendetrabajo',
            name='orden_de_trabajo',
            field=models.OneToOneField(related_name='cotizacion', to='orden_de_trabajo.OrdenDeTrabajo'),
        ),
    ]
