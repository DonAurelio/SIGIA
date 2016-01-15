# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
        ('orden_de_trabajo', '0003_auto_20160115_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotizacionOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalles', models.TextField()),
                ('costo', models.FloatField()),
                ('fecha_vencimiento', models.DateField()),
                ('habilitado', models.BooleanField(default=True)),
                ('orden_de_trabajo', models.OneToOneField(to='orden_de_trabajo.OrdenDeTrabajo')),
                ('repuestos', models.ManyToManyField(to='repuesto.Repuesto')),
            ],
            options={
                'ordering': ['fecha_vencimiento'],
                'verbose_name_plural': 'Cotizaciones Ordenes de Trabajo',
            },
        ),
    ]
