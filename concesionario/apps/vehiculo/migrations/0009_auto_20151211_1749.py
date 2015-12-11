# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
        ('vehiculo', '0008_auto_20151210_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='SucursalVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
            ],
            options={
                'ordering': ['cantidad'],
                'verbose_name_plural': 'Vehiculos Sucursal',
            },
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='sucursalvehiculo',
            name='vehiculo',
            field=models.ForeignKey(to='vehiculo.Vehiculo'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='sucursal_vehiculos',
            field=models.ManyToManyField(to='sucursal.Sucursal', through='vehiculo.SucursalVehiculo'),
        ),
    ]
