# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
        ('empleado', '0008_auto_20151206_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.OneToOneField(default=None, to='sucursal.Sucursal'),
            preserve_default=False,
        ),
    ]
