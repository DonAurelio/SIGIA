"""concesionario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
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
    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    #se deseas colocar imagenes en tu contenido HTML, este link es necesario para que se muestren las imagenes
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
]
