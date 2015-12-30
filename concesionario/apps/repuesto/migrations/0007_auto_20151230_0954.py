# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0006_auto_20151211_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repuesto',
            name='habilitado',
        ),
        migrations.AddField(
            model_name='sucursalrepuesto',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
