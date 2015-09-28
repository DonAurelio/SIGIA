# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=20, null=True, blank=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('salario', models.BigIntegerField(null=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenes/cuenta/vendedor', blank=True)),
                ('sucursal', models.OneToOneField(default=None, to='sucursal.Sucursal')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
