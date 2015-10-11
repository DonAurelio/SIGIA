# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_auto_20151001_0431'),
        ('cliente', '0001_initial'),
        ('empleado', '0003_auto_20150930_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_venta', models.DateField()),
                ('descuento', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('forma_pago', models.CharField(default=b'Efectivo', max_length=20, choices=[(b'Credito', b'Credito'), (b'Efectivo', b'Efectivo'), (b'Tarjeta_credito', b'Tarjeta de credito'), (b'Tarjeta_debito', b'Tarjeta de debito')])),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('empleado', models.ForeignKey(to='empleado.Empleado')),
                ('vehiculo', models.ForeignKey(to='vehiculo.Vehiculo')),
            ],
            options={
                'ordering': ['fecha_venta'],
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
