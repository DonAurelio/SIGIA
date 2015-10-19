# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0002_auto_20151019_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='nombre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
