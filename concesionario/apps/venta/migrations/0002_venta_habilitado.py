# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
