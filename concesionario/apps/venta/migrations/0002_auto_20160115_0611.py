# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
