# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura_orden_trabajo', '0002_facturaordentrabajo_orden_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaordentrabajo',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
