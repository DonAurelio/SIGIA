# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='fecha_salida',
            field=models.DateField(null=True),
        ),
    ]
