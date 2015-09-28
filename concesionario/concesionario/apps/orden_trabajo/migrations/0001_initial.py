# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repuesto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaOrdenTrabajo',
            fields=[
                ('id_factura_orden_trabajo', models.AutoField(serialize=False, primary_key=True)),
                ('costo_mano_obra', models.BigIntegerField()),
                ('costo_repuestos', models.BigIntegerField()),
                ('costo_total', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id_orden_trabajo', models.AutoField(serialize=False, primary_key=True)),
                ('placa_vehiculo', models.CharField(max_length=7, null=True, blank=True)),
                ('fecha_entrada', models.DateField(auto_now=True)),
                ('fecha_salida', models.DateField()),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField()),
                ('cliente', models.OneToOneField(to='cliente.Cliente')),
                ('empleado', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='facturaordentrabajo',
            name='orden_trabajo',
            field=models.OneToOneField(to='orden_trabajo.OrdenTrabajo'),
        ),
        migrations.AddField(
            model_name='facturaordentrabajo',
            name='repuestos',
            field=models.ManyToManyField(to='repuesto.Repuesto'),
        ),
    ]
