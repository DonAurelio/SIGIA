# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
        ('vehiculo', '0006_vehiculo_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal_Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidades', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=60)),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='sucursal_vehiculo',
            name='vehiculo',
            field=models.ForeignKey(to='vehiculo.Vehiculo'),
        ),
    ]
