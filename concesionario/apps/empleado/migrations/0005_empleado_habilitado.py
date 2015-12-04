# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0004_auto_20151204_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
