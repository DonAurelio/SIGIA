# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_compra', models.DateTimeField(auto_now=True, null=True)),
                ('precio_venta', models.BigIntegerField(null=True, blank=True)),
                ('descuento', models.FloatField(null=True, blank=True)),
                ('forma_pago', models.CharField(default=b'Efectivo', max_length=20, choices=[(b'Efectivo', b'Efectivo'), (b'Tarjeta_credito', b'Tarjeta de credito'), (b'Tarjeta_debito', b'Tarjeta de debito')])),
            ],
        ),
    ]
