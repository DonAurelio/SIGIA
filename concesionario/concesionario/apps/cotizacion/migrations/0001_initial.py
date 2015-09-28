# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id_cotizacion', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('forma_pago', models.CharField(default=b'Efectivo', max_length=20, choices=[(b'Efectivo', b'Efectivo'), (b'Tarjeta_credito', b'Tarjeta de credito'), (b'Tarjeta_debito', b'Tarjeta de debito')])),
                ('cliente', models.OneToOneField(to='cliente.Cliente')),
                ('empleado', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('vehiculo', models.OneToOneField(to='vehiculo.Vehiculo')),
            ],
        ),
    ]
