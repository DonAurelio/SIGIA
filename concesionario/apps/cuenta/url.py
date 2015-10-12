# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import Editar
from .views import EditarContrasenia 
from .views import Perfil

urlpatterns = [
	#Redirecciona la peticion a la vista que permite modificar el perfil del usuario de django y empleado
	url(r'^cuenta/editar$', Editar.as_view(), name='editar'),
	#Redirecciona la peticion a la vista que permite modificar la contraseña de usuario
	url(r'^cuenta/editar_contrasenia$', EditarContrasenia.as_view(), name='editar_contrasenia'),
	#Redirecciona la peticion a la vista que permite visualizar el perfil de usuario
	url(r'^cuenta/perfil$', Perfil.as_view(), name='perfil'),
    
]