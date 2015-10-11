# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(default=b'Beige', max_length=50, choices=[(b'Automovil', b'Automovil'), (b'Negro', b'Negro'), (b'Blanco', b'Blanco'), (b'Beige', b'Beige'), (b'Gris', b'Gris'), (b'Azul', b'Azul'), (b'Amarillo', b'Amarillo'), (b'Rojo', b'Rojo'), (b'Verde', b'Verde')]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo',
            field=models.CharField(default=b'Automovil', max_length=50, choices=[(b'Automovil', b'Automovil'), (b'Campero', b'Campero'), (b'Camioneta', b'Camioneta'), (b'Microbus', b'Microbus'), (b'Buseta', b'Buseta'), (b'Bus', b'Bus'), (b'Camion', b'Camion'), (b'Tracto camion', b'Tracto camion')]),
        ),
    ]
