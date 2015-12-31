# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0011_auto_20151231_1042'),
        ('repuesto', '0011_auto_20151231_1042'),
        ('sucursal', '0007_remove_sucursal_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='SucursalRepuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('repuesto', models.ForeignKey(to='repuesto.Repuesto')),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
            ],
            options={
                'ordering': ['cantidad'],
                'verbose_name_plural': 'Repuestos Sucursal',
            },
        ),
        migrations.CreateModel(
            name='SucursalVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
                ('vehiculo', models.ForeignKey(to='vehiculo.Vehiculo')),
            ],
            options={
                'ordering': ['cantidad'],
                'verbose_name_plural': 'Vehiculos Sucursal',
            },
        ),
        migrations.AddField(
            model_name='sucursal',
            name='repuestos',
            field=models.ManyToManyField(to='repuesto.Repuesto', through='sucursal.SucursalRepuesto'),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='vehiculos',
            field=models.ManyToManyField(to='vehiculo.Vehiculo', through='sucursal.SucursalVehiculo'),
        ),
    ]
