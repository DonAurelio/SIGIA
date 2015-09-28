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
                ('id_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('departamento', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=20, null=True, blank=True)),
            ],
        ),
    ]
