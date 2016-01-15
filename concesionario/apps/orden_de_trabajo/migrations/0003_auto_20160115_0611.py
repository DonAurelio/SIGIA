# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0002_auto_20160114_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='estado_reparacion',
            field=models.TextField(default=b'Pendiente', max_length=50, null=True, blank=True, choices=[(b'Pendiente', b'Pendiente'), (b'Cotizado', b'Cotizado'), (b'Reparado', b'Reparado'), (b'Retirado', b'Retirado')]),
        ),
    ]
