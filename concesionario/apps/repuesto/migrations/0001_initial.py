# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('marca', models.CharField(max_length=20)),
                ('clasificacion', models.CharField(default=b'Sellos_empaques', max_length=20, choices=[(b'Automotriz', b'Automotriz'), (b'Ferreteria', b'Ferreteria'), (b'Pinturas', b'Pinturas'), (b'Rodamientos', b'Rodamientos'), (b'Solventes', b'Solventes'), (b'Bandas_cadenas', b'Bandas y cadenas'), (b'Limpieza', b'Limpieza'), (b'Autopartes', b'Autopartes'), (b'Sellos_empaques', b'Sellos y empaques'), (b'Lubricantes', b'Lubricantes')])),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'imagenes/repuestos/')),
                ('proveedor', models.ForeignKey(to='proveedor.Proveedor')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Repuestos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='repuesto',
            unique_together=set([('nombre', 'proveedor')]),
        ),
    ]
