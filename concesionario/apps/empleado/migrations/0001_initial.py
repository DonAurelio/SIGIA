# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(unique=True, max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
                ('salario', models.BigIntegerField()),
                ('tipo', models.CharField(default=b'Vendedor', max_length=20, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente')])),
                ('habilitado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(upload_to=b'imagenes/empleado')),
                ('sucursal', models.ForeignKey(to='sucursal.Sucursal')),
                ('user', models.OneToOneField(related_name='empleado', default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['identificacion'],
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
