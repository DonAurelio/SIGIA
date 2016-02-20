# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20160128_0401'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sucursal',
            unique_together=set([('nombre', 'ciudad')]),
        ),
    ]
