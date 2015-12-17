# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0005_auto_20151216_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'imagenes', blank=True),
        ),
    ]
