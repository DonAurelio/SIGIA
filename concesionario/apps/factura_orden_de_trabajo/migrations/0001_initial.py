# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo_total', models.FloatField(default=0)),
                ('cotizacion', models.OneToOneField(related_name='factura', to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo')),
            ],
            options={
                'verbose_name_plural': 'Facturas de Ordenes de Trabajo',
            },
        ),
    ]
