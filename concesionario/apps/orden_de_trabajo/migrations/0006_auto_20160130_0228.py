# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orden_de_trabajo', '0005_auto_20160124_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='placa',
            field=models.CharField(blank=True, max_length=7, null=True, validators=[django.core.validators.RegexValidator(b'^[A-Z]{3}-[0-9]{3}', message=b'Debe ingresar una placa valida ej: ABC-123', code=b'Invalid Key')]),
        ),
    ]
