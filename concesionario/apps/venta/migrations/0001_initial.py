# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('sucursal', '0001_initial'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('precio_venta', models.FloatField()),
                ('forma_pago', models.CharField(default=b'Efectivo', max_length=20, choices=[(b'Credito', b'Credito'), (b'Efectivo', b'Efectivo'), (b'Tarjeta_credito', b'Tarjeta de credito'), (b'Tarjeta_debito', b'Tarjeta de debito')])),
                ('habilitado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('empleado', models.ForeignKey(related_name='ventas', to='empleado.Empleado')),
                ('sucursal_vehiculo', models.ForeignKey(related_name='ventas', to='sucursal.SucursalVehiculo')),
            ],
            options={
                'ordering': ['fecha_venta'],
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
