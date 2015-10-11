# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('empleado', '0003_auto_20150930_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=6, null=True, blank=True)),
                ('fecha_entrada', models.DateField(null=True, blank=True)),
                ('fecha_salida', models.DateField(null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('estado_reparacion', models.CharField(max_length=50, null=True, blank=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('empleado', models.ForeignKey(to='empleado.Empleado')),
            ],
            options={
                'ordering': ['fecha_entrada'],
                'verbose_name_plural': 'ordendetrabajo',
            },
        ),
    ]
