# -*- encoding: utf-8 -*-

from django.conf.urls import include, url

from . import views


urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    url(r'^empleado/crear$',views.nuevo_usuario, name='crear'),
    url(r'^empleado/crearEmpleado$', views.nuevo_empleado, name='crearEmpleado'),
      
]
