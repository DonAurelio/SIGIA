# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('sucursal', '0001_initial'),
        ('empleado', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(b'^[A-Z]{3}-[0-9]{3}', message=b'Debe ingresar una placa valida ej: ABC-123', code=b'Invalid Key')])),
                ('fecha_entrada', models.DateField(auto_now_add=True)),
                ('fecha_salida', models.DateField()),
                ('estado_reparacion', models.TextField(default=b'Pendiente', max_length=50, choices=[(b'Pendiente', b'Pendiente'), (b'Cotizado', b'Cotizado'), (b'Reparado', b'Reparado'), (b'Reparado y entregado', b'Reparado y entregado'), (b'Retirado', b'Retirado')])),
                ('observacion', models.TextField(max_length=200)),
                ('habilitado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('empleado', models.ForeignKey(to='empleado.Empleado')),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
                ('vehiculo', models.ForeignKey(to='vehiculo.Vehiculo')),
            ],
            options={
                'ordering': ['fecha_entrada'],
                'verbose_name_plural': 'Orden de Trabajo',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ordendetrabajo',
            unique_together=set([('placa', 'fecha_salida')]),
        ),
    ]
