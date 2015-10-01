# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_serie', models.CharField(max_length=100, null=True, blank=True)),
                ('marca', models.CharField(max_length=100, null=True, blank=True)),
                ('precio', models.FloatField(null=True, blank=True)),
                ('modelo', models.CharField(max_length=100, null=True, blank=True)),
                ('potencia', models.CharField(max_length=100, null=True, blank=True)),
                ('motor', models.CharField(max_length=100, null=True, blank=True)),
                ('caracteristicas', models.TextField(null=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/vehiculos/', blank=True)),
                ('capacidad', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(default=b'Automovil', max_length=2, choices=[(b'Automovil', b'Automovil'), (b'Campero', b'Campero'), (b'Camioneta', b'Camioneta'), (b'Microbus', b'Microbus'), (b'Buseta', b'Buseta'), (b'Bus', b'Bus'), (b'Camion', b'Camion'), (b'Tracto camion', b'Tracto camion')])),
            ],
        ),
    ]
