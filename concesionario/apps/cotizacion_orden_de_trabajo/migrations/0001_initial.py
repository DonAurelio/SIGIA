# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
        ('orden_de_trabajo', '0005_auto_20160124_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotizacionOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalles', models.TextField()),
                ('costo_reparacion', models.FloatField()),
                ('fecha_vencimiento', models.DateField()),
                ('habilitado', models.BooleanField(default=True)),
                ('orden_de_trabajo', models.OneToOneField(related_name='cotizacion', to='orden_de_trabajo.OrdenDeTrabajo')),
            ],
            options={
                'ordering': ['fecha_vencimiento'],
                'verbose_name_plural': 'Cotizaciones Ordenes de Trabajo',
            },
        ),
        migrations.CreateModel(
            name='RepuestoCantidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('cotizacion_orden_de_trabajo', models.ForeignKey(related_name='repuestos_cantidad', to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo')),
                ('repuesto', models.ForeignKey(to='repuesto.Repuesto')),
            ],
            options={
                'verbose_name_plural': 'Repuestos Cantidad',
            },
        ),
        migrations.AlterUniqueTogether(
            name='repuestocantidad',
            unique_together=set([('cotizacion_orden_de_trabajo', 'repuesto')]),
        ),
    ]
