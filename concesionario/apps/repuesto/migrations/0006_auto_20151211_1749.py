# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0004_auto_20151204_1614'),
        ('repuesto', '0005_repuesto_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='SucursalRepuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['cantidad'],
                'verbose_name_plural': 'Repuestos Sucursal',
            },
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='sucursalrepuesto',
            name='repuesto',
            field=models.ForeignKey(to='repuesto.Repuesto'),
        ),
        migrations.AddField(
            model_name='sucursalrepuesto',
            name='sucursal',
            field=models.ForeignKey(to='sucursal.Sucursal'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='sucursal_repuestos',
            field=models.ManyToManyField(to='sucursal.Sucursal', through='repuesto.SucursalRepuesto'),
        ),
    ]
