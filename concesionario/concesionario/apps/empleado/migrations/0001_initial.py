# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=20, unique=True, null=True, blank=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('salario', models.BigIntegerField(null=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/cuenta/empleado', blank=True)),
                ('tipo', models.CharField(default=b'Vendedor', max_length=20, choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['identificacion'],
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
