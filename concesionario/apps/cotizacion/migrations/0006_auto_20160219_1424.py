# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_auto_20160114_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(related_name='cotizaciones', default=None, to='cliente.Cliente'),
        ),
    ]
