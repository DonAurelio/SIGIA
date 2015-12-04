# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_auto_20150930_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='direccion',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='identificacion',
            field=models.CharField(unique=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
