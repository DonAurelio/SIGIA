from django.db import models
from django.contrib.auth.models import User
from concesionario.apps.sucursal.models import Sucursal
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

User.add_to_class('identificacion',models.CharField(max_length=20,null=True,blank=True))
User.add_to_class('sucursal', models.OneToOneField(Sucursal))
User.add_to_class('direccion', models.CharField(null=True,blank=True,max_length=200))
User.add_to_class('telefono', models.CharField(null=True,blank=True,max_length=10))
User.add_to_class('salario', models.BigIntegerField(null=True,blank=True)),
User.add_to_class('foto', models.ImageField(null=True,blank=True,upload_to = "imagenes/cuenta"))
User.add_to_class('thumbnail', ImageSpecField(source='foto',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60}))


VENDEDOR = 'Vendedor'
JEFE_TALLER = 'Jefe de taller'
GERENTE = 'Gerente'

tipo = (
	(VENDEDOR, 'Vendedor'),
	(JEFE_TALLER, 'Jefe de taller'),
	(GERENTE, 'Gerente'),
)

User.add_to_class('tipousuario' ,models.CharField(max_length=20, choices=tipo,default=VENDEDOR))
