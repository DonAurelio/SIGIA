# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id_repuesto', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('precio', models.BigIntegerField()),
                ('marca', models.CharField(max_length=100, null=True, blank=True)),
                ('proveedor', models.CharField(max_length=100, null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/repuestos', blank=True)),
                ('clasificacion', models.CharField(default=b'Automotriz', max_length=100, null=True, blank=True, choices=[(b'Automotriz', b'Automotriz'), (b'Ferreteria', b'Ferreteria'), (b'Pinturas', b'Pinturas'), (b'Rodamientos', b'Rodamientos'), (b'Solventes', b'Solventes'), (b'Bandas y Cadenas', b'Bandas y Cadenas'), (b'Limpieza', b'Limpieza'), (b'Autopartes', b'Autopartes'), (b'Sellos y Empaques', b'Sellos y Empaques')])),
            ],
        ),
    ]
