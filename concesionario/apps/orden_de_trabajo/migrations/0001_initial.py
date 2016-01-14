# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_habilitado'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=7, null=True, blank=True)),
                ('fecha_entrada', models.DateField(auto_now_add=True, null=True)),
                ('fecha_salida', models.DateField(null=True, blank=True)),
                ('estado_reparacion', models.TextField(default=b'Pendiente', max_length=50, null=True, blank=True, choices=[(b'Pendiente', b'Pendiente'), (b'En observacion', b'En observacion'), (b'En reparacion', b'En reparacion'), (b'Finalizado', b'Finalizado')])),
                ('observacion', models.TextField(max_length=200, null=True, blank=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(default=None, to='cliente.Cliente')),
                ('empleado', models.ForeignKey(default=None, to='empleado.Empleado')),
            ],
            options={
                'ordering': ['fecha_entrada'],
                'verbose_name_plural': 'Orden de Trabajo',
            },
        ),
    ]
