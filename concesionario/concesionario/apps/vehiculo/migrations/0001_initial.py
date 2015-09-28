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
                ('numero_serie', models.AutoField(serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=50, null=True, blank=True)),
                ('precio', models.BigIntegerField(null=True, blank=True)),
                ('modelo', models.IntegerField(null=True, blank=True)),
                ('potencia', models.IntegerField(null=True, blank=True)),
                ('motor', models.CharField(max_length=50, null=True, blank=True)),
                ('caracteristicas', models.TextField(null=True, blank=True)),
                ('capacidad', models.IntegerField(null=True, blank=True)),
                ('color', models.CharField(max_length=50, null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/vehiculos', blank=True)),
                ('tipo', models.CharField(default=b'Automovil', max_length=100, null=True, blank=True, choices=[(b'Automovil', b'AUTOMOVIL'), (b'Campero', b'CAMPERO'), (b'Camioneta', b'CAMIONETA'), (b'Microbus', b'MICROBUS'), (b'Buseta', b'BUSETA'), (b'Bus Metropolitano', b'BUS METROPOLITANO'), (b'Camion mediano F-350', b'CAMION MEDIANO F350'), (b'Camion Grade F-600', b'CAMION GRADE F600'), (b'Camion C3', b'CAMION C3'), (b'Tracto Camion', b'TRACTO CAMION'), (b'Camion C4', b'CAMION C4')])),
            ],
        ),
    ]
