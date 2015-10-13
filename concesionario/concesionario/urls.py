# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from concesionario import settings

urlpatterns = [
	#url para el acceso al sitio de administracion
    url(r'^admin/', include(admin.site.urls)),
    #Inclusion de las url que hay en la aplicacion inicio
    url(r'', include('apps.inicio.url',namespace='inicio')),
    #Inclusion de las url que hay en la aplicacion cuenta
    url(r'', include('apps.cuenta.url',namespace='cuenta')),
    #Inclusion de las url que hay en la aplicacion cotizacion
    url(r'', include('apps.cotizacion.url',namespace='cotizacion')),
    #Inclusion de las url que hay en la aplicacion cliente
    url(r'', include('apps.cliente.url',namespace='cliente')),
    #Inclusion de las url que hay en la aplicacion empleado
    url(r'', include('apps.empleado.url',namespace='empleado')),
    #Inclusion de las url que hay en la aplicacion factura_orden_trabajo
    #url(r'', include('apps.factura_orden_trabajo.url',namespace='factura_orden_trabajo')),
    #Inclusion de las url que hay en la aplicacion orden_de_trabajo
    #url(r'', include('apps.orden_de_trabajo.url',namespace='orden_de_trabajo')),
    #Inclusion de las url que hay en la aplicacion repuesto
    url(r'', include('apps.repuesto.url',namespace='repuesto')),
    #Inclusion de las url que hay en la aplicacion sucursal
    #url(r'', include('apps.sucursal.url',namespace='sucursal')),
    #Inclusion de las url que hay en la aplicacion vehiculo
    #url(r'', include('apps.vehiculo.url',namespace='vehiculo')),
    #Inclusion de las url que hay en la aplicacion venta
    #url(r'', include('apps.venta.url',namespace='venta')),

    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    #se deseas colocar imagenes en tu contenido HTML, este link es necesario para que se muestren las imagenes
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #Para la recuperacion de la cuenta usando los templates de django

    #Envia al formuario para confirmar el correo de la persona que olvido su login
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password'),
    #Muestra un aviso que indica que ha sido enviado un mensaje al correo electronico
    #dicho mensaje tendra un link temporal que permitira mostrar un formulario de recuperacion de contraseña
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    #Procesa la url generada para recuperar el login del usuario
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    #muestra un mensaje donde de confirma exitosamente que se ha completado el proceso de reperación del login
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

]
