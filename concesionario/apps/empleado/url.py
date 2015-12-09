# -*- encoding: utf-8 -*-

from django.conf.urls import include, url

from . import views


urlpatterns = [

    #url que redirecciona a la pagina de creacion de cotizaciones 
    #url(r'^empleado/crear$',views.nuevo_usuario, name='crear'),
    url(r'^empleado/crear$',views.EmpleadoCreateView.as_view(), name='crear'),
    url(r'^empleado/(?P<pk>\d+)/$', views.EmpleadoUpdateView.as_view(), name='actualizar'),
]
