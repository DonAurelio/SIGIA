# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0003_auto_20160115_0611'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ordendetrabajo',
            unique_together=set([('placa', 'fecha_salida')]),
        ),
    ]
