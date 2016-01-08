# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_auto_20160107_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
