# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0003_auto_20151204_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sucursal',
            old_name='activo',
            new_name='habilitado',
        ),
    ]
