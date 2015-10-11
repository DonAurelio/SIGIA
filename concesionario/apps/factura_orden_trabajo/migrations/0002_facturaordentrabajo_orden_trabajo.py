# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0001_initial'),
        ('factura_orden_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaordentrabajo',
            name='orden_trabajo',
            field=models.OneToOneField(default=None, to='orden_de_trabajo.OrdenDeTrabajo'),
            preserve_default=False,
        ),
    ]
