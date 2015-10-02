# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordendetrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=6, null=True, blank=True)),
                ('fecha_entrada', models.DateField(null=True, blank=True)),
                ('fecha_salida', models.DateField(null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('estado_reparacion', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['fecha_entrada'],
                'verbose_name_plural': 'ordendetrabajo',
            },
        ),
    ]
