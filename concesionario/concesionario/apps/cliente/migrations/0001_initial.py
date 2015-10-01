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
                ('identificacion', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('apellido', models.CharField(max_length=100, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=100, null=True, blank=True)),
                ('departamento', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('celular', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
            ],
            options={
                'ordering': ['apellido'],
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
