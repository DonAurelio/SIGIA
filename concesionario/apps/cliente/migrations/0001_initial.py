# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['apellido'],
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
