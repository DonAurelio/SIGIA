# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_auto_20160115_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
