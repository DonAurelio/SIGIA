# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('cotizacion', '0002_remove_cotizacion_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='cliente',
            field=models.OneToOneField(default=None, to='cliente.Cliente'),
        ),
    ]
