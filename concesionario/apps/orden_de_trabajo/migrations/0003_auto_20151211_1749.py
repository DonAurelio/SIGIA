# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0002_auto_20151204_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordendetrabajo',
            name='estado_vehiculo',
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='estado_reparacion',
            field=models.CharField(default=b'Pendiente', max_length=50, null=True, blank=True, choices=[(b'Pendiente', b'Pendiente'), (b'En observacion', b'En observacion'), (b'En reparacion', b'En reparacion'), (b'Finalizado', b'Finalizado')]),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='observacion',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='placa',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
    ]
