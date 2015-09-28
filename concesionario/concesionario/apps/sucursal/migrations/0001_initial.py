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
                ('id_sucursal', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('repuestos', models.ManyToManyField(to='repuesto.Repuesto')),
                ('vehiculos', models.ManyToManyField(to='vehiculo.Vehiculo')),
            ],
        ),
    ]
