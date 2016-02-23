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
                ('nombre', models.CharField(unique=True, max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=50)),
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
                ('cantidad', models.IntegerField()),
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
                ('color', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
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
            field=models.ManyToManyField(related_name='sucursal', through='sucursal.SucursalRepuesto', to='repuesto.Repuesto'),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='vehiculos',
            field=models.ManyToManyField(related_name='sucursal', through='sucursal.SucursalVehiculo', to='vehiculo.Vehiculo'),
        ),
        migrations.AlterUniqueTogether(
            name='sucursalvehiculo',
            unique_together=set([('sucursal', 'vehiculo', 'color')]),
        ),
        migrations.AlterUniqueTogether(
            name='sucursalrepuesto',
            unique_together=set([('sucursal', 'repuesto')]),
        ),
        migrations.AlterUniqueTogether(
            name='sucursal',
            unique_together=set([('nombre', 'ciudad')]),
        ),
    ]
