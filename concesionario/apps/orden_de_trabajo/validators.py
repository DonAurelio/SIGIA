# -*- encoding: utf-8 -*-

from django.core.validators import RegexValidator

validador_placa = RegexValidator(
                    r'^[A-Z]{3}-[0-9]{3}',
                    message='Debe ingresar una placa valida ej: ABC-123',
                    code='Invalid Key')