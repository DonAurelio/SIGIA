# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Sucursales',
            },
        ),
    ]
