# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion_orden_de_trabajo', '0002_auto_20160119_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo_total', models.FloatField()),
                ('cotizacion', models.OneToOneField(to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo')),
            ],
            options={
                'verbose_name_plural': 'Facturas de Ordenes de Trabajo',
            },
        ),
    ]
