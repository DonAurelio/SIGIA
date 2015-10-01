# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'ordering': ['numero_serie'], 'verbose_name_plural': 'Vehiculos'},
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(default=b'Beige', max_length=2, choices=[(b'Automovil', b'Automovil'), (b'Negro', b'Negro'), (b'Blanco', b'Blanco'), (b'Beige', b'Beige'), (b'Gris', b'Gris'), (b'Azul', b'Azul'), (b'Amarillo', b'Amarillo'), (b'Rojo', b'Rojo'), (b'Verde', b'Verde')]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='motor',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
