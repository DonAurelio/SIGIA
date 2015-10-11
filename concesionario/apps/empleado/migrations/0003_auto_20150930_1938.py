# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_auto_20150930_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(related_name='empleado', to=settings.AUTH_USER_MODEL),
        ),
    ]
