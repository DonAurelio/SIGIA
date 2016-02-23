# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from .views import Login, Logout
from .views import RecuperarLogin
from .views import RecuperarLoginEmailEnviado
from .views import RecuperarLoginConfirmacion
from .views import RecuperarLoginTerminado

urlpatterns = [

	#Para el inicio y cierre que sesion
	url(r'^$', Login.as_view(), name='login'),
	url(r'^inicio/login/$', Login.as_view(), name='login'),
	url(r'^inicio/logout/$', Logout.as_view(), name='logout'),

	#Para la recuperacion de la cuenta

    #Envia al formuario para confirmar el correo de la persona que olvido su login
    url(r'^inicio/recuperar_login/$', RecuperarLogin.as_view(), name='recuperar_login'),
    #Muestra un aviso que indica que ha sido enviado un mensaje al correo electronico
    #dicho mensaje tendra un link temporal que permitira mostrar un formulario de recuperacion de contraseña
    url(r'^inicio/recuperar_login_email_enviado/$', RecuperarLoginEmailEnviado.as_view(), name='recuperar_login_email_enviado'),
    #Procesa la url generada para recuperar el login del usuario
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', RecuperarLoginConfirmacion.as_view(), name='recuperar_login_confirmacion'),
    #muestra un mensaje donde se confirma  que se ha completado el proceso de reperación del login
    url(r'^inicio/recuperar_login_terminado$', RecuperarLoginTerminado.as_view(), name='recuperar_login_terminado'),
]
