# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sucursal', '0001_initial'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(to='sucursal.Sucursal'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(related_name='empleado', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
