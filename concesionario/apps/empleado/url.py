# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^empleado/sucursal/crear/(?P<spk>\d+)/$',views.EmpleadoCreateView.as_view(), name='crear'),
    url(r'^empleado/sucursal/actualizar/(?P<epk>\d+)/(?P<spk>\d)/$', views.EmpleadoUpdateView.as_view(), name='actualizar'),
    url(r'^empleado/sucursal/listado/(?P<spk>\d+)/$', views.EmpleadoListView.as_view(), name='listar-empleados-sucursal'),
]
