from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

User.add_to_class('identificacion',models.PositiveIntegerField(null=True,blank=True))
User.add_to_class('direccion', models.FloatField(null=True,blank=True))
User.add_to_class('telefono', models.PositiveIntegerField(null=True,blank=True))
User.add_to_class('foto', models.ImageField(null=True,blank=True,upload_to = "imagenes"))
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