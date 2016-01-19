# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
        ('cotizacion_orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepuestoCantidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Repuestos Cantidad',
            },
        ),
        migrations.RemoveField(
            model_name='cotizacionordendetrabajo',
            name='repuestos',
        ),
        migrations.AddField(
            model_name='repuestocantidad',
            name='cotizacion_orden_de_trabajo',
            field=models.ForeignKey(to='cotizacion_orden_de_trabajo.CotizacionOrdenDeTrabajo'),
        ),
        migrations.AddField(
            model_name='repuestocantidad',
            name='repuesto',
            field=models.ForeignKey(to='repuesto.Repuesto'),
        ),
    ]
