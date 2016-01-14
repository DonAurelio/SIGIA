# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(unique=True, max_length=20, blank=True)),
                ('direccion', models.CharField(max_length=200, blank=True)),
                ('telefono', models.CharField(max_length=10, blank=True)),
                ('salario', models.BigIntegerField(blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/empleado', blank=True)),
                ('tipo', models.CharField(default=b'Vendedor', max_length=20, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente')])),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['identificacion'],
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
