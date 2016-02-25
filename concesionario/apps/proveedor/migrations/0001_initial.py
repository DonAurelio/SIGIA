# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
