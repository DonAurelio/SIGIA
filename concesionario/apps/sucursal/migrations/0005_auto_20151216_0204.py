# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='nombre',
            field=models.CharField(max_length=20, unique=True, null=True, blank=True),
        ),
    ]
