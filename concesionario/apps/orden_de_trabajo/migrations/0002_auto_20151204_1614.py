# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordendetrabajo',
            old_name='estado_reparacion',
            new_name='estado_vehiculo',
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
