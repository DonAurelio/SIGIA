from django.conf.urls import include, url
from django.contrib import admin
from concesionario import settings

urlpatterns = [
	#url para el acceso al sitio de administracion
    url(r'^admin/', include(admin.site.urls)),
    #Inclusion de las url que hay en la aplicacion inicio
    url(r'', include('concesionario.apps.inicio.url',namespace='inicio')),
    #Inclusion de las url que hay en la aplicacion cuenta
    url(r'', include('concesionario.apps.cuenta.url',namespace='cuenta')),
    #Inclusion de las url que hay en la aplicacion cotizacion
    url(r'', include('concesionario.apps.cotizacion.url',namespace='cotizacion')),
    #Inclusion de las url que hay en la aplicacion cliente
    url(r'', include('concesionario.apps.cliente.url',namespace='cliente')),
    #Inclusion de las url que hay en la aplicacion empleado
    url(r'', include('concesionario.apps.empleado.url',namespace='empleado')),
    #Inclusion de las url que hay en la aplicacion factura_orden_trabajo
    url(r'', include('concesionario.apps.factura_orden_trabajo.url',namespace='factura_orden_trabajo')),
    #Inclusion de las url que hay en la aplicacion orden_de_trabajo
    url(r'', include('concesionario.apps.orden_de_trabajo.url',namespace='orden_de_trabajo')),
    #Inclusion de las url que hay en la aplicacion repuesto
    url(r'', include('concesionario.apps.repuesto.url',namespace='repuesto')),
    #Inclusion de las url que hay en la aplicacion sucursal
    url(r'', include('concesionario.apps.sucursal.url',namespace='sucursal')),
    #Inclusion de las url que hay en la aplicacion vehiculo
    url(r'', include('concesionario.apps.vehiculo.url',namespace='vehiculo')),
    #Inclusion de las url que hay en la aplicacion venta
    url(r'', include('concesionario.apps.venta.url',namespace='venta')),

    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    #se deseas colocar imagenes en tu contenido HTML, este link es necesario para que se muestren las imagenes
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
