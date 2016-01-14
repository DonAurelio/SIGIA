# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from concesionario import settings

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.inicio.url',namespace='inicio')),
    url(r'', include('apps.cuenta.url',namespace='cuenta')),
    url(r'', include('apps.cotizacion.url',namespace='cotizacion')),
    url(r'', include('apps.cliente.url',namespace='cliente')),
    url(r'', include('apps.empleado.url',namespace='empleado')),
    url(r'', include('apps.repuesto.url',namespace='repuesto')),
    url(r'', include('apps.sucursal.url',namespace='sucursal')),
    url(r'', include('apps.vehiculo.url',namespace='vehiculo')),
    url(r'', include('apps.venta.url',namespace='venta')),
    url(r'', include('apps.proveedor.url',namespace='proveedor')),
    url(r'', include('apps.orden_de_trabajo.url',namespace='orden_de_trabajo')),

    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    #se deseas colocar imagenes en tu contenido HTML, este link es necesario para que se muestren las imagenes
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

]
