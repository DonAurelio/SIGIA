# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0004_repuesto_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
