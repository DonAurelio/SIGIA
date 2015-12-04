# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0003_auto_20151204_0409'),
        ('repuesto', '0003_auto_20151019_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='sucursal',
            field=models.ManyToManyField(to='sucursal.Sucursal'),
        ),
    ]
