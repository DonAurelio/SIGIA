# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_empleado_habilitado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(related_name='empleado', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
