# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repuesto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repuesto',
            old_name='provedor',
            new_name='proveedor',
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='clasificacion',
            field=models.CharField(default=b'Sellos_empaques', max_length=20, null=True, blank=True, choices=[(b'Automotriz', b'Automotriz'), (b'Ferreteria', b'Ferreteria'), (b'Pinturas', b'Pinturas'), (b'Rodamientos', b'Rodamientos'), (b'Solventes', b'Solventes'), (b'Bandas_cadenas', b'Bandas y cadenas'), (b'Limpieza', b'Limpieza'), (b'Autopartes', b'Autopartes'), (b'Sellos_empaques', b'Sellos y empaques'), (b'Lubricantes', b'Lubricantes')]),
        ),
    ]
