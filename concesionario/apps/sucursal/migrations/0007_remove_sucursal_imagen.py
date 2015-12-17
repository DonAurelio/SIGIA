# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0006_sucursal_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='imagen',
        ),
    ]
