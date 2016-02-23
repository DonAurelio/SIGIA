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
                ('numero_serie', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('modelo', models.CharField(max_length=100)),
                ('potencia', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=200)),
                ('caracteristicas', models.TextField()),
                ('capacidad', models.CharField(max_length=50)),
                ('tipo', models.CharField(default=b'Automovil', max_length=50, choices=[(b'Automovil', b'Automovil'), (b'Campero', b'Campero'), (b'Camioneta', b'Camioneta'), (b'Microbus', b'Microbus'), (b'Buseta', b'Buseta'), (b'Bus', b'Bus'), (b'Camion', b'Camion'), (b'Tracto camion', b'Tracto camion')])),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/vehiculos/', blank=True)),
            ],
            options={
                'ordering': ['numero_serie'],
                'verbose_name_plural': 'Vehiculos',
            },
        ),
    ]
