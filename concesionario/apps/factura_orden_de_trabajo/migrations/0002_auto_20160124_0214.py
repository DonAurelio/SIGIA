# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura_orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaordendetrabajo',
            name='cotizacion',
            field=models.OneToOneField(related_name='factura', to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo'),
        ),
    ]
