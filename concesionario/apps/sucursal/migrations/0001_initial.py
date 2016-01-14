# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('repuesto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20, unique=True, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Sucursales',
            },
        ),
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
        migrations.AlterUniqueTogether(
            name='sucursalvehiculo',
            unique_together=set([('sucursal', 'vehiculo', 'color')]),
        ),
    ]
