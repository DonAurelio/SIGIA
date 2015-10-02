# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaOrdenTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo_mano_obra', models.FloatField(null=True, blank=True)),
                ('costo_repuestos', models.FloatField(null=True, blank=True)),
                ('costo_total', models.FloatField(null=True, blank=True)),
                ('repuestos', models.ManyToManyField(to='repuesto.Repuesto')),
            ],
        ),
    ]
